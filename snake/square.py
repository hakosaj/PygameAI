
import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller



class Square:


    def __init__(self,xcoord,ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.x = xcoord*blocksize
        self.y = ycoord*blocksize
        self.food=False


    def setFood(self,bol):
        self.food=bol
    
    def drawSquare(self):
        ro=pygame.Rect(self.x,self.y,blocksize,blocksize)
        ri=pygame.Rect(self.x+1,self.y+1,blocksize-1,blocksize-1)
        pygame.draw.rect(screen,BLACK,ro)
        if (self.food):
            pygame.draw.rect(screen,GREEN,ri)
        else:
            pygame.draw.rect(screen,BLACK,ri)



    def drawSnakeSquare(self):
        ro=pygame.Rect(self.x,self.y,blocksize,blocksize)
        ri=pygame.Rect(self.x+1,self.y+1,blocksize-1,blocksize-1)
        pygame.draw.rect(screen,BLACK,ro)
        pygame.draw.rect(screen,RED,ri)