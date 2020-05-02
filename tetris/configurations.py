
import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller

#configurations = i j t o s z l

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

def generateOConfiguration(xp,yp,offset,grid):
    squares=[]
    squares.append(grid.elementAt(xp,yp))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(0)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(1)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(2)%8))
    return squares

def generateZConfiguration(xp,yp,offset,grid):
    squares=[]
    squares.append(grid.elementAt(xp,yp))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(3+offset)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(4+offset)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(6+offset)%8))
    return squares

def generateSConfiguration(xp,yp,offset,grid):
    squares=[]
    squares.append(grid.elementAt(xp,yp))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(2+offset)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(4+offset)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(5+offset)%8))
    return squares

def generateLConfiguration(xp,yp,offset,grid):
    squares=[]
    squares.append(grid.elementAt(xp,yp))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(2+offset)%8))
    squares.append(grid.neighborAt(grid.elementAt(xp,yp),(6+offset)%8))
    lastN = grid.neighborAt(grid.elementAt(xp,yp),(6+offset)%8)
    squares.append(grid.neighborAt(lastN,(6+offset)%8))
    return squares

    

    

    

    

    
