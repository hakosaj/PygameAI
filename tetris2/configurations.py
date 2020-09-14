
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




def createConfiguration(xp,yp,offset,grid, configuration):
    try:
        grid.clearMovingBlocks()
        offset=offset%8
        if (configuration=="j"):
            generateJConfiguration(xp,yp,offset,grid)
        elif (configuration=="l"):
            generateLConfiguration(xp,yp,offset,grid)
        elif (configuration=="t"):
            generateTConfiguration(xp,yp,offset,grid)
        elif (configuration=="o"):
            generateOConfiguration(xp,yp,offset,grid)
        elif (configuration=="z"):
            generateZConfiguration(xp,yp,offset,grid)
        elif (configuration=="s"):
            generateSConfiguration(xp,yp,offset,grid)

        #Rightmove collision
        if xp>14 or grid.xDifference()>4:
            return False
        #Leftmove collision
        if xp<0 or grid.xDifference()>4:
            return False
        #Downmove collision
        if yp>29 or grid.yDifference()>4:
            return False
        return True
    except AttributeError:
        return False
    #Type 1 block collision
    except AssertionError:
        return False




def generateJConfiguration(xp,yp,offset,grid):
    grid.changeStatus(grid.elementAt(xp,yp),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(offset%8)),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(4+offset)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(5+offset)%8),2)
def generateLConfiguration(xp,yp,offset,grid):
    grid.changeStatus(grid.elementAt(xp,yp),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(offset%8)),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(4+offset)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(3+offset)%8),2)
def generateTConfiguration(xp,yp,offset,grid):
    grid.changeStatus(grid.elementAt(xp,yp),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(2+offset)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(4+offset)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(6+offset)%8),2)

def generateOConfiguration(xp,yp,offset,grid):
    grid.changeStatus(grid.elementAt(xp,yp),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(0)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(1)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(2)%8),2)

def generateZConfiguration(xp,yp,offset,grid):
    grid.changeStatus(grid.elementAt(xp,yp),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(3+offset)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(4+offset)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(6+offset)%8),2)

def generateSConfiguration(xp,yp,offset,grid):
    grid.changeStatus(grid.elementAt(xp,yp),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(2+offset)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(4+offset)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(5+offset)%8),2)

def generateLConfiguration(xp,yp,offset,grid):
    grid.changeStatus(grid.elementAt(xp,yp),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(2+offset)%8),2)
    grid.changeStatus(grid.neighborAt(grid.elementAt(xp,yp),(6+offset)%8),2)
    lastN = grid.neighborAt(grid.elementAt(xp,yp),(6+offset)%8)
    grid.changeStatus(grid.neighborAt(lastN,(6+offset)%8),2)







    

    

    
