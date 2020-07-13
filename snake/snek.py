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
        self.squares.append(self.grid.elementAt(x,y+1))
        self.squares.append(self.grid.elementAt(x,y+2))
        self.squares.append(self.grid.elementAt(x,y+3))
        self.movement=0
        self.dead=False


    def drawSnake(self):
        for item in self.squares:
            item.drawSnakeSquare()


    def moveSnake(self):
        newSquare = self.grid.neighborAt(self.squares[0],self.movement)
        self.squares.insert(0,newSquare)
        self.squares.pop(-1)

        if self.grid.checkCollision(self.squares):
            self.dead=True
            print("Snek is dead:( \nYou tried to cross over yourself.")


    def changeOrientation(self,orientation):
        if (abs(self.movement-orientation)!=4):
            self.movement=orientation
        else:
            self.dead=True
            print("Snek is dead:( \nYou tried to turn inside yourself.")


