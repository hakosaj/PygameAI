
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


class Grid:

    def __init__(self,x,y):
        self.x0=x
        self.y0=y
        self.squares=[]
        self.blocks=[]


    def createSquares(self):
        for xn in range(self.x0):
            col=[]
            for yn in range(self.y0):
                col.append(Square(xn,yn))
            self.squares.append(col)


    def modifyBlock(self,block):
        block.rotateBlock()
        self.addBlock(block)

    def addBlock(self,block):
        for item in self.squares:
            for sub in item:
                sub.clearAssignment()
        self.blocks.append(block)
        for block in self.blocks:
            for item in block.squares:
                item.assignToBlock(block)

    def removeBlock(self,block):
        self.blocks.remove(block)
        for item in self.squares:
            for sub in item:
                sub.clearAssignment()

    def elementAt(self,x,y):
        try:
            return self.squares[x][y]
        except IndexError:
            print("Grid index out of bounds")
            return None



    def neighborAt(self,square,orientation):
        xs=square.xcoord
        ys=square.ycoord
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

    def drawGrid(self):
        for item in self.squares:
            for subitem in item:
                subitem.drawSquare()

    def printGrid(self):
        for j in range(self.y0):
            for i in range(self.x0):
                square = self.elementAt(i,j)
                if (square.assignedBlock!=None):
                    print("x",end='')
                else:
                    print("_",end='')
            print("\n",end='')


            

