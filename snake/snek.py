import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller
from grid import *


class Snek:

    def __init__(self,x,y,gr):
        self.x0=x
        self.y0=y
        self.grid=gr
        self.squares=[]
        self.squares.append(self.grid.elementAt(x,y))
        self.movement=0
        self.dead=False


    def drawSnake(self):
        for item in self.squares:
            item.drawSnakeSquare()


    def moveSnake(self):
        self.squares.append(self.grid.neighborAt(self.squares[0],self.movement))
        self.squares.pop(0)


    def changeOrientation(self,orientation):
        self.movement=orientation


