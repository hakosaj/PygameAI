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
from configurations import *


def upKey(xCur,yCur,offset,g,currentOne,currentColor):
    if (currentOne=="l"):
        if not ((offset==2 and xCur>12) or (offset==6 and xCur>13) ):
            if createConfiguration(xCur,yCur,offset+2,g,currentOne):
                offset+=2
            else:
                createConfiguration(xCur,yCur,offset,g,currentOne)

    else:
        if (currentOne!="o"):
            if createConfiguration(xCur,yCur,offset+2,g,currentOne):
                offset+=2
            else:
                createConfiguration(xCur,yCur,offset,g,currentOne)
    return xCur,yCur,currentOne,currentColor,False,g,offset

def rightKey(xCur,yCur,offset,g,currentOne,currentColor):
    if createConfiguration(xCur+1,yCur,offset,g,currentOne):
        xCur+=1
    else:
        createConfiguration(xCur,yCur,offset,g,currentOne)
    return xCur,yCur,currentOne,currentColor,False,g,offset

def leftKey(xCur,yCur,offset,g,currentOne,currentColor):
    if createConfiguration(xCur-1,yCur,offset,g,currentOne):
        xCur-=1
    else:
        createConfiguration(xCur,yCur,offset,g,currentOne)
    return xCur,yCur,currentOne,currentColor,False,g,offset

def downKey(xCur,yCur,offset,g,currentOne,currentColor):
    if createConfiguration(xCur,yCur+1,offset,g,currentOne):
        yCur+=1
        return xCur,yCur,currentOne,currentColor,False,g,offset
    else:
        rets= g.spawnBlock(xCur,yCur,offset,g,currentOne,currentColor)
        createConfiguration(rets[0],rets[1],rets[6],rets[5],rets[2])
        return rets

def spaceKey(xCur,yCur,offset,g,currentOne,currentColor):
    while createConfiguration(xCur,yCur+1,offset,g,currentOne):
        yCur+=1
    rets= g.spawnBlock(xCur,yCur,offset,g,currentOne,currentColor)
    createConfiguration(rets[0],rets[1],rets[6],rets[5],rets[2])
    #params=downKey(xCur,yCur, offset, g, currentOne, currentColor)
    return rets
    #return g.spawnBlock(xCur,yCur,offset,g,currentOne,currentColor)
