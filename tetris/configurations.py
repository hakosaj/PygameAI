
import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller


def generateJConfiguration(xp,yp,offset,grid):
    squares=[]
    squares.append(grid.elementAt(xp,yp))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(offset%8)))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(4+offset)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(5+offset)%8))
    return squares
def generateLConfiguration(xp,yp,offset,grid):
    squares=[]
    squares.append(grid.elementAt(xp,yp))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(offset%8)))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(4+offset)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(3+offset)%8))
    return squares
def generateTConfiguration(xp,yp,offset,grid):
    squares=[]
    squares.append(grid.elementAt(xp,yp))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(2+offset)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(4+offset)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(6+offset)%8))
    return squares