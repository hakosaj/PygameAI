
import sys
import os
import random
import time
import pygame
import math
from configurations import *
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
        self.color = RED
        self.offset=0
        self.isStopped=False


    def stop(self):
        self.isStopped=True

    def collidesWith(self,block):
        for sq1 in self.squares:
            for sq2 in block.squares:
                if sq1.xcoord==sq2.xcoord and sq1.ycoord==sq2.ycoord:
                    return True
        return False

    #Anna perusblokki ekana, sitten muut suhteessa tähän. Rotateblock j siirtää kaikkia 2 eteenpäin
    def createConfiguration(self,offset):
        xp=self.x
        yp=self.y
        self.offset=(self.offset+offset)%8
        print("conf: ",self.configuration, " offset: ",self.offset)
        if (self.configuration=="j"):
            self.squares.extend(generateJConfiguration(xp,yp,self.offset,self.grid))
        elif (self.configuration=="l"):
            self.squares.extend(generateLConfiguration(xp,yp,self.offset,self.grid))
        elif (self.configuration=="t"):
            self.squares=generateTConfiguration(xp,yp,self.offset,self.grid)
        elif (self.configuration=="o"):
            self.squares=generateOConfiguration(xp,yp,self.offset,self.grid)
        elif (self.configuration=="z"):
            self.squares=generateZConfiguration(xp,yp,self.offset,self.grid)
        elif (self.configuration=="s"):
            self.squares=generateZConfiguration(xp,yp,self.offset,self.grid)
        elif (self.configuration=="l"):
            self.squares=generateZConfiguration(xp,yp,self.offset,self.grid)


        else:
            print("nuh uh")

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
        try:
            if abs(self.rightEdge()-self.leftEdge())>4:
                self.clearSquares()
                self.createConfiguration(-2)
        except AttributeError:
            self.createConfiguration(-2)
        if self.squares.count(None):
            print("none!!!!")
            return 0
        else:
            return 1



    



