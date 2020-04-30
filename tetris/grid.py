
import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller




class Grid:

    def __init__(self,x,y):
        self.x0=x
        self.y0=y
        self.squares=[]


    def createSquares(self):
        for xn in range(self.x0):
            col=[]
            for yn in range(self.y0):
                col.append(False)
            self.squares.append(col)

    def drawGrid(self):
        x=0
        y=0
        for item in self.squares:
            for subitem in item:
                ro=pygame.Rect(x,y,blocksize,blocksize)
                ri=pygame.Rect(x+1,y+1,blocksize-1,blocksize-1)
                pygame.draw.rect(screen,BLACK,ro)
                pygame.draw.rect(screen,WHITE,ri)
                y=y+blocksize
            y=0
            x=x+blocksize
            

