
import sys
import os
import random
import time
import pygame
import math
import random
from square import *
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller


class Grid:

    def __init__(self,x,y,walls):
        self.x0=x
        self.y0=y
        self.squares=[]
        self.foodsquare = Square(0,0)
        self.walls=walls

    def randomFood(self):
        self.foodsquare.setFood(False)
        self.foodsquare=self.elementAt(random.randint(0,gridsizex-1),random.randint(0,gridsizey-1))
        while (self.foodsquare.snake):
            self.foodsquare=self.elementAt(random.randint(0,gridsizex-1),random.randint(0,gridsizey-1))
        self.foodsquare.setFood(True)

    def createSquares(self):
        for xn in range(self.x0):
            col=[]
            for yn in range(self.y0):
                col.append(Square(xn,yn))
            self.squares.append(col)


    def walledElementAt(self,x,y):
        if x>=gridsizex or y>=gridsizey or x<0 or y<0:
            return None
        else:
            a=x
            b=y
            return self.squares[a][b]

    def elementAt(self,x,y):
        if (walls):
            return self.walledElementAt(x,y)
        a=x
        b=y
        if x==gridsizex:
            a=0
        if y==gridsizey:
            b=0
        return self.squares[a][b]



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

    def checkCollision(self, squares, newsquare):
        for item in squares:
            if item.x==newsquare.x and item.y==newsquare.y:
                return True

        return False


            

