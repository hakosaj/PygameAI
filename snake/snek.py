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
        self.grid.elementAt(x,y).snake=True
        #self.movement=0
        self.movement=random.randrange(0,7,2)
        self.dead=False



    def hed(self):
        return self.squares[0]

    def moveSnake(self):
        eaten=False
        newSquare = self.grid.neighborAt(self.squares[0],self.movement)
        if self.grid.walls:
            if (newSquare==None):
                self.dead=True
                if (importantPrints):
                    print("Snek crashed into a wall")
                return eaten

            if (abs(self.squares[0].xcoord-newSquare.xcoord)>2) or (abs(self.squares[0].ycoord-newSquare.ycoord)>2):
                self.dead=True
                if importantPrints:
                    print("Snek crashed into a wall")
                return eaten


        if self.grid.checkCollision(self.squares,newSquare):
            self.dead=True
            if importantPrints:
                print("Snek is dead:( \nYou tried to cross over yourself.")
            return eaten
        else:
            if newSquare.food:
                self.grid.randomFood()
                eaten=True
            else:
                self.squares[-1].snake=False
                self.squares.pop(-1)

            self.squares.insert(0,newSquare)
            newSquare.snake=True
            return eaten


    def changeOrientation(self,orientation):
        if (abs(self.movement-orientation)!=4):
            self.movement=orientation
            return True
        return False


