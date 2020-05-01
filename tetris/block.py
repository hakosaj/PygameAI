
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

    #Anna perusblokki ekana, sitten muut suhteessa tähän. Rotateblock j siirtää kaikkia 2 eteenpäin
    def createConfiguration(self):
        if (self.configuration=="j"):
            xp=self.x
            yp=self.y+1
            self.squares.append(self.grid.elementAt(xp,yp))
            self.squares.append(self.grid.neighborAt(self.grid.elementAt(xp,yp),1))
            self.squares.append(self.grid.neighborAt(self.grid.elementAt(xp,yp),5))
            self.squares.append(self.grid.neighborAt(self.grid.elementAt(xp,yp+1),7))


    #def rotateBlock


        



