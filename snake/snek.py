import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from grid import *


class Snek:

    def __init__(self,x,y,gr):
        """Initialize the snake

        Args:
            x (int): start position
            y (int): start position y
            gr (Grid): game grid
        """
        self.x0=x
        self.y0=y
        self.grid=gr
        self.squares=[]
        self.squares.append(self.grid.elementAt(x,y))
        self.grid.elementAt(x,y).snake=True
        #self.movement=0
        self.movement=random.randrange(0,7,2)
        self.dead=False
        self.indexTable=[[0] * gr.x0 for i in range(gr.y0)]

    def hed(self):
        """Snake head

        Returns:
            Square: first square of the snake
        """
        return self.squares[0]

    def resetIndexTable(self):
        """Reset hamiltionian path index table
        """
        self.indexTable=[[0] * self.grid.x0 for i in range(self.grid.y0)]

    def tail(self):
        """Snake tail

        Returns:
            Square: last square of the snake
        """
        return self.squares[-1]


    def body(self):
        """Snake body excluding head and tail

        Returns:
            [Square]: list of squares the body consists of
        """
        return self.squares[1:-1]


    def length(self):
        """Length of the snake

        Returns:
            int: length
        """
        return len(self.squares)

    def moveSnake(self):
        """Move snake and do all the collision/food checks

        Returns:
            bool: snake ate food or not
        """
        eaten = False
        newSquare = self.grid.neighborAt(self.squares[0], self.movement)
        if self.grid.walls:
            if newSquare == None:
                self.dead = True
                if importantPrints:
                    print("Snek crashed into a wall")
                return eaten

            if (abs(self.squares[0].xcoord - newSquare.xcoord) > 2) or (
                abs(self.squares[0].ycoord - newSquare.ycoord) > 2
            ):
                self.dead = True
                if importantPrints:
                    print("Snek crashed into a wall")
                return eaten

        if self.grid.checkCollision(self.squares, newSquare):
            self.dead = True
            if importantPrints:
                print("Snek is dead:( \nYou tried to cross over yourself.")
            return eaten
        else:
            if newSquare.food:
                self.grid.randomFood()
                eaten = True
            else:
                self.squares[-1].snake = False
                self.squares.pop(-1)

            self.squares.insert(0, newSquare)
            newSquare.snake = True
            return eaten

    def changeOrientation(self, orientation):
        """Make sure snake cannot turn backwards

        Args:
            orientation (int): orientatio

        Returns:
            bool: can turn or not
        """
        if abs(self.movement - orientation) != 4:
            self.movement = orientation
            return True
        return False
