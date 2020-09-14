
import sys
import os
import random
import time
import pygame
import math
from block import Block
from square import *
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller
from configurations import *
from collections import Iterable


class Grid:

    def __init__(self,x,y,loselimit):
        self.x0=x
        self.y0=y
        self.squares=[]
        self.loselimit=loselimit


    def createSquares(self):
        for xn in range(self.x0):
            col=[]
            for yn in range(self.y0):
                col.append(Square(xn,yn))
            self.squares.append(col)

#    def modifyBlock(self,block):
#        a = block
#        a.rotateBlock()
#        self.removeBlock(block)
#        self.addBlock(a)


#    def addBlock(self,block):
#        for item in self.squares:
#            for sub in item:
#                sub.clearAssignment()
#        self.blocks.append(block)
#        for block in self.blocks:
#            for item in block.squares:
#                item.assignToBlock(block)

#    def removeBlock(self,block):
#        self.blocks.remove(block)
        #for item in block.squares:
            #for sub in item:
                #sub.clearAssignment()

    def elementAt(self,x,y):
        try:
            return self.squares[x][y]
        except IndexError:
            return None



    def neighborAt(self,square,orientation):
        xs=square.xcoord
        ys=square.ycoord
        #print(orientation)
        if(orientation==0):
            return self.elementAt(xs,ys-1)
        elif(orientation==1):
            return self.elementAt(xs+1,ys-1)
        elif(orientation==2):
            return self.elementAt(xs+1,ys)
        elif(orientation==3):
            return self.elementAt(xs+1,ys+1)
        elif(orientation==4):
            return self.elementAt(xs,ys+1)
        elif(orientation==5):
            return self.elementAt(xs-1,ys+1)
        elif(orientation==6):
            return self.elementAt(xs-1,ys)
        elif(orientation==7):
            return self.elementAt(xs-1,ys-1)
        else:
            print("Not a valid orientation")
            return square

    def drawGrid(self,currentColor):
        for item in self.squares:
            for subitem in item:
                subitem.drawSquare(currentColor)
        pygame.draw.rect(screen,BLACK,pygame.Rect(300,0,170,height))
        pygame.draw.rect(screen,(150,150,150),pygame.Rect(0,0,300,120))

    def changeStatus(self,square,newStatus):
        if square.status!=1:
            square.changeStatus(newStatus)
        else:
            raise AssertionError

    def forceChangeStatus(self,square,newStatus):
        square.changeStatus(newStatus)

    def clearMovingBlocks(self):
        for item in self.squares:
            for sq in item:
                if sq.status!=1:
                    self.changeStatus(sq,0)

    def movingBlockMinX(self):
        sqs = filter(lambda x: x.status==2,[item for sublist in self.squares for item in sublist])
        return min(map(lambda x:x.xcoord,sqs))
        
    def movingBlockMaxX(self):
        sqs = filter(lambda x: x.status==2,[item for sublist in self.squares for item in sublist])
        return max(map(lambda x:x.xcoord,sqs))

    
    def xDifference(self):
        return abs(self.movingBlockMaxX()-self.movingBlockMinX())

    def movingBlockMinY(self):
        sqs = filter(lambda x: x.status==2,[item for sublist in self.squares for item in sublist])
        return min(map(lambda x:x.ycoord,sqs))
        
    def movingBlockMaxY(self):
        sqs = filter(lambda x: x.status==2,[item for sublist in self.squares for item in sublist])
        return max(map(lambda x:x.ycoord,sqs))

    
    def yDifference(self):
        return abs(self.movingBlockMaxY()-self.movingBlockMinY())

    def activesToLanded(self,col):
        sqs = filter(lambda x: x.status==2,[item for sublist in self.squares for item in sublist])
        for item in sqs:
            self.changeStatus(item,1)
            item.changeColor(col)
            if item.ycoord<self.loselimit:
                raise UnboundLocalError
        r=300
        b=300
        g=300
        while (r+g+b>550):
            r=random.randint(1,250)
            g=random.randint(1,250)
            b=random.randint(1,250)
        return pygame.Color((r,g,b))



    def clearScore(self,rows):
        if rows==1:
            return 40
        elif rows==2:
            return 100
        elif rows==3:
            return 300
        else:
            return 1200

    def removeFullRows(self):
        count=0
        clearedRows=0
        for j in range(self.y0):
            for i in range(self.x0):
                if self.elementAt(i,j).status==1:
                    count+=1
            if count==15:
                self.removeSingleRow(j)
                clearedRows+=1
            count=0
        if clearedRows>0:
            print(f"Cleared {clearedRows} rows")
            return self.clearScore(clearedRows)
        return 0


    def removeSingleRow(self,row):
        for i in range (self.x0):
            self.forceChangeStatus(self.elementAt(i,row),0)
        self.shiftAllLanded(row)

    def shiftAllLanded(self,row):
        #Jos status 1 ja alla tyhjää, siirrä alaspäin. Alkaen ylhäältä
        for j in range (row-1,0,-1):
            for i in range(self.x0):
                if self.elementAt(i,j).status==1:
                    self.forceChangeStatus(self.elementAt(i,j),0)
                    self.forceChangeStatus(self.elementAt(i,j+1),1)
                    self.elementAt(i,j+1).color=self.elementAt(i,j).color



    def printGrid(self):
        for j in range(self.y0):
            for i in range(self.x0):
                square = self.elementAt(i,j)
                if (square.status!=0):
                    print("x",end='')
                else:
                    print("_",end='')
            print("\n",end='')



    def spawnBlock(self,xCur,yCur,offset,g,currentOne,currentColor,currentOnes):
            createConfiguration(xCur,yCur,offset,g,currentOne)
            try:
                currentColor=g.activesToLanded(currentColor)
                xCur=xstart
                yCur=ystart
                currentOne=random.choice(currentOnes)
                return xCur,yCur, currentOne, currentColor, False
            except UnboundLocalError:
                return xCur,yCur, currentOne, currentColor, True