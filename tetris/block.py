
import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller



#configurations = i j l o s z t

class Block:

    def __init__(self,x,y,configuration,grid):
        self.x=x
        self.y=y
        self.grid=grid
        self.configuration = configuration
        self.squares=[]
        self.rotation = 0
        self.color = RED
        self.offset=0

    #Anna perusblokki ekana, sitten muut suhteessa tähän. Rotateblock j siirtää kaikkia 2 eteenpäin
    def createConfiguration(self,offset):
        if (self.configuration=="j"):
            xp=self.x
            yp=self.y
            self.offset=(self.offset+offset)%8
            print("configuration: ",self.offset)
            self.squares.append(self.grid.elementAt(xp,yp))
            self.squares.append(self.grid.neighborAt(self.grid.elementAt(xp,yp),(self.offset%8)))
            self.squares.append(self.grid.neighborAt(self.grid.elementAt(xp,yp),(4+self.offset)%8))
            self.squares.append(self.grid.neighborAt(self.grid.elementAt(xp,yp),(5+self.offset)%8))
    

    def rightEdge(self):
        return max(bl.x for bl in self.squares)/blocksize
    def leftEdge(self):
        return min(bl.x for bl in self.squares)/blocksize
    def bottomEdge(self):
        return max(bl.y for bl in self.squares)/blocksize

    def clearSquares(self):
        self.squares.clear()
        

    def shiftBlock(self,dir):
        if (dir==1):
            self.x=self.x+blocksize
            self.clearSquares()
            self.createConfiguration(0)
        elif (dir==2):
            self.y=self.y+blocksize
        elif (dir==3):
            self.x=self.x-blocksize


    def rotateBlock(self):
        self.clearSquares()
        self.createConfiguration(2)


        



