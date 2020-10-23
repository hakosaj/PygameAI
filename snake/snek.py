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
        newSquare = self.grid.neighborAt(self.squares[0],self.movement)
        if self.grid.walls:
            if (abs(self.squares[0].xcoord-newSquare.xcoord)>2) or (abs(self.squares[0].ycoord-newSquare.ycoord)>2):
                self.dead=True
                print("Snek crashed into a wall")


        if self.grid.checkCollision(self.squares,newSquare):
            self.dead=True
            print("Snek is dead:( \nYou tried to cross over yourself.")
        else:
            if newSquare.food:
                self.grid.randomFood()
            else:
                self.squares.pop(-1)

            self.squares.insert(0,newSquare)


    def changeOrientation(self,orientation):
        if (abs(self.movement-orientation)!=4):
            self.movement=orientation


