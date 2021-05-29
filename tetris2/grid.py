import sys
import os
import random
import time
import pygame
import math
import copy
from square import *
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller
from configurations import *
from collections import Iterable


class Grid:
    def __init__(self, x, y, loselimit, agent):
        """Game grid

        Args:
            x (int): grid size x
            y (int): grid size y
            loselimit (int): where does the game become lost
            agent (AIAgent): ai agent
        """
        self.x0 = x
        self.y0 = y
        self.squares = []
        self.loselimit = loselimit
        self.agent = agent
        self.currentBag = copy.deepcopy(currentOnes)

    def createSquares(self):
        """Create all the grid squares"""
        for xn in range(self.x0):
            col = []
            for yn in range(self.y0):
                col.append(Square(xn, yn))
            self.squares.append(col)

    #    def modifyBlock(self,block):
    #        a = block
    #        a.rotateBlock()
    #        self.removeBlock(block)
    #        self.addBlock(a

    def elementAt(self, x, y):
        """Element at

        Args:
            x (int): xcoodd
            y (int): ycoord

        Returns:
            Square: neighbor square
        """
        try:
            return self.squares[x][y]
        except IndexError:
            return None

    def neighborAt(self, square, orientation):
        """Neighbor of this square to a given orientation

        Args:
            square (Square): square
            orientation (int): orientation

        Returns:
            Square: neighbor square
        """
        xs = square.xcoord
        ys = square.ycoord
        # print(orientation)
        if orientation == 0:
            return self.elementAt(xs, ys - 1)
        elif orientation == 1:
            return self.elementAt(xs + 1, ys - 1)
        elif orientation == 2:
            return self.elementAt(xs + 1, ys)
        elif orientation == 3:
            return self.elementAt(xs + 1, ys + 1)
        elif orientation == 4:
            return self.elementAt(xs, ys + 1)
        elif orientation == 5:
            return self.elementAt(xs - 1, ys + 1)
        elif orientation == 6:
            return self.elementAt(xs - 1, ys)
        elif orientation == 7:
            return self.elementAt(xs - 1, ys - 1)
        else:
            print("Not a valid orientation")
            return square

    def drawGrid(self, currentColor):
        """Draw the tetris grid

        Args:
            currentColor ([Int]): color
        """
        for item in self.squares:
            for subitem in item:
                subitem.drawSquare(currentColor)
        pygame.draw.rect(screen, BLACK, pygame.Rect(300, 0, 220, height))
        pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(0, 0, 300, 120))

    def changeStatus(self, square, newStatus):
        """Change square status

        Args:
            square (Square): square
            newStatus (int): new status

        Raises:
            AssertionError: Square status not expected
        """
        if square.status != 1:
            square.changeStatus(newStatus)
        else:
            raise AssertionError

    def forceChangeStatus(self, square, newStatus):
        square.changeStatus(newStatus)

    def clearMovingBlocks(self):
        """Clear all moving blocks"""
        for item in self.squares:
            for sq in item:
                if sq.status != 1:
                    # self.changeStatus(sq,0)
                    sq.status = 0

    def movingBlockMinX(self):
        """Minimum x for the block

        Returns:
            int: min x
        """
        sqs = filter(
            lambda x: x.status == 2,
            [item for sublist in self.squares for item in sublist],
        )
        return min(map(lambda x: x.xcoord, sqs))

    def movingBlockMaxX(self):
        """Max x for the block

        Returns:
            int: max x
        """
        sqs = filter(
            lambda x: x.status == 2,
            [item for sublist in self.squares for item in sublist],
        )
        return max(map(lambda x: x.xcoord, sqs))

    def xDifference(self):
        """Total x difference of the block

        Returns:
            int: x diff
        """
        sqs = list(
            map(
                lambda g: g.xcoord,
                filter(
                    lambda x: x.status == 2,
                    [item for sublist in self.squares for item in sublist],
                ),
            )
        )
        return abs(max(sqs) - min(sqs))

    def yDifference(self):
        """Total y difference of the block

        Returns:
            int: y diff
        """
        sqs = list(
            map(
                lambda g: g.ycoord,
                filter(
                    lambda x: x.status == 2,
                    [item for sublist in self.squares for item in sublist],
                ),
            )
        )
        return abs(max(sqs) - min(sqs))

    def diffs(self):
        """Differences in x and y

        Returns:
            (int): x and y diffs
        """
        sqs = list(
            filter(
                lambda x: x.status == 2,
                [item for sublist in self.squares for item in sublist],
            )
        )
        xs = list(map(lambda g: g.xcoord, sqs))
        ys = list(map(lambda g: g.ycoord, sqs))
        return (
            abs(max(xs) - min(xs)),
            abs(max(ys) - min(ys)),
        )

    def movingBlockMinY(self):
        """minimum y in move

        Returns:
            int: minimum y
        """
        sqs = filter(
            lambda x: x.status == 2,
            [item for sublist in self.squares for item in sublist],
        )
        return min(map(lambda x: x.ycoord, sqs))

    def movingBlockMaxY(self):
        """Max y of moving block

        Returns:
            int: max y
        """
        sqs = filter(
            lambda x: x.status == 2,
            [item for sublist in self.squares for item in sublist],
        )
        return max(map(lambda x: x.ycoord, sqs))

    def activesToLanded(self, col):
        """Active blocks to landed blocks

        Args:
            col ([int]): color

        Raises:
            UnboundLocalError: Game is lost

        Returns:
            pygame.Color: color
        """
        sqs = filter(
            lambda x: x.status == 2,
            [item for sublist in self.squares for item in sublist],
        )
        for item in sqs:
            self.changeStatus(item, 1)
            item.changeColor(col)
            if item.ycoord < self.loselimit:
                raise UnboundLocalError
        r = 300
        b = 300
        g = 300
        while r + g + b > 450:
            r = random.randint(1, 250)
            g = random.randint(1, 250)
            b = random.randint(1, 250)
        return pygame.Color((r, g, b))

    def clearScore(self, rows):
        """Give score based on lines cleared

        Args:
            rows (int): rows cleared

        Returns:
            int: score
        """
        if rows == 1:
            return 40
        elif rows == 2:
            return 100
        elif rows == 3:
            return 300
        else:
            return 1200

    def removeFullRows(self):
        """Remove full rows from the blocks

        Returns:
            int: score from cleared
        """
        count = 0
        clearedRows = 0
        for j in range(self.y0):
            for i in range(self.x0):
                if self.elementAt(i, j).status == 1:
                    count += 1
            if count == 15:
                self.removeSingleRow(j)
                clearedRows += 1
            count = 0
        if clearedRows > 0:
            # print(f"Cleared {clearedRows} rows")
            return self.clearScore(clearedRows)
        return 0

    def removeSingleRow(self, row):
        """Remove a singular row

        Args:
            row (int): row number
        """
        for i in range(self.x0):
            self.forceChangeStatus(self.elementAt(i, row), 0)
        self.shiftAllLanded(row)

    def shiftAllLanded(self, row):
        """Shift landed rows if removed from below them

        Args:
            row (int): row above which to shift down
        """
        # Jos status 1 ja alla tyhjää, siirrä alaspäin. Alkaen ylhäältä
        for j in range(row - 1, 0, -1):
            for i in range(self.x0):
                if self.elementAt(i, j).status == 1:
                    self.forceChangeStatus(self.elementAt(i, j), 0)
                    self.forceChangeStatus(self.elementAt(i, j + 1), 1)
                    self.elementAt(i, j + 1).color = self.elementAt(i, j).color

    def printGrid(self):
        """Pring tetris grid state"""
        for j in range(self.y0):
            for i in range(self.x0):
                square = self.elementAt(i, j)
                if square.status == 2:
                    print("2", end="")
                elif square.status == 1:
                    print("1", end="")
                else:
                    print("_", end="")
            print("\n", end="")
        print("\n", end="")
        print(self.totalHeight())
        print(self.bumpiness())
        print(self.virtualFullRows())
        print(self.holes())

    def spawnBlock(self, xCur, yCur, offset, g, currentOne, currentColor, manual):
        """Spawn a new block and calculate the optimal movement

        Args:
            xCur (int): current x coord of the new block
            yCur (int): current y coord of the new block
            offset (int): orientation offset
            g (Grid): game grid
            currentOne (char): shape of the piece
            currentColor ([int]): block color
            manual (bool): manual or auto

        Returns:
            int, int, char, [int],bool,Grid,int: new game state
        """
        starttime = time.time()
        createConfiguration(xCur, yCur, offset, g, currentOne)
        try:
            currentColor = g.activesToLanded(currentColor)
            xCur = xstart
            yCur = ystart
            # Print the current one

            # currentOne=random.choice(currentOnes)

            self.currentBag.remove(currentOne)
            if len(self.currentBag) == 0:
                self.currentBag = copy.deepcopy(currentOnes)
            currentOne = random.choice(self.currentBag)

            createConfiguration(xCur, yCur, offset, g, currentOne)
            agenttime = time.time()
            if not manual:
                params = [xCur, yCur, currentOne, currentColor, False, self, offset]
                self.agent.calculateMovement(*params)
                endtime = time.time()
                print(f"Agenttime: {endtime-agenttime}")
            return xCur, yCur, currentOne, currentColor, False, self, offset
        except UnboundLocalError:
            endtime = time.time()
            return xCur, yCur, currentOne, currentColor, True, self, offset

    def totalScoring(self):
        """AI weight scoring of the current grid

        Returns:
            float,float,int,float: game scoring status
        """
        totalheight = 0
        rowStates = [0] * self.y0
        totalHoles = 0
        bumps = 0
        heights = [0] * self.x0
        for i in range(self.x0):
            colheight = 0
            holeflag = False
            heightflag = False
            for j in range(self.y0):
                if self.elementAt(i, j).status == 1:
                    # Bumpiness
                    # Total height
                    if not heightflag:
                        totalheight += self.y0 - j
                        heights[i] = self.y0 - j
                        heightflag = True

                    # Virtual full rows
                    rowStates[j] = rowStates[j] + 1

                    # holes
                    holeflag = True
                if holeflag:
                    if self.elementAt(i, j).status == 0:
                        totalHoles += 1

        for p in range(self.x0 - 1):
            bumps += abs(heights[p + 1] - heights[p])

        return totalheight, rowStates.count(self.x0), totalHoles, bumps

    def totalHeight(self):
        """Total height of the current grid

        Returns:
            int: height
        """
        h = 0
        for i in range(self.x0):
            for j in range(self.y0):
                if self.elementAt(i, j).status == 1:
                    h += self.y0 - j
                    break
        return h

    def virtualFullRowsReverse(self):
        """Get virtual full rows count

        Returns:
            int: count
        """
        rowStates = [0] * self.y0
        for i in range(self.x0):
            for j in range(self.y0):
                if self.elementAt(i, j).status == 1:
                    rowStates[j] = rowStates[j] + 1
        return rowStates.count(self.x0)

    def virtualFullRows(self):
        """Get virtuak full rows count

        Returns:
            [type]: [description]
        """
        count = 0
        fullRows = 0
        for j in range(self.y0):
            for i in range(self.x0):
                if self.elementAt(i, j).status == 1:
                    count += 1
            if count == 15:
                fullRows += 1
            count = 0
        return fullRows

    def holes(self):
        """Hole amount

        Returns:
            int: holes
        """
        holes = 0
        for i in range(self.x0):
            found = False
            for j in range(self.y0):
                if self.elementAt(i, j).status == 1:
                    found = True
                if found:
                    if self.elementAt(i, j).status == 0:
                        holes += 1
        return holes

    def bumpiness(self):
        """Current grid bumpiness

        Returns:
            float: bumpiness
        """
        bmp = 0
        heights = []
        for i in range(self.x0):
            colheight = 0
            for j in range(self.y0):
                if self.elementAt(i, j).status == 1:
                    colheight += self.y0 - j
                    break
            heights.append(colheight)
        for p in range(self.x0 - 1):
            bmp += abs(heights[p + 1] - heights[p])
        return bmp
