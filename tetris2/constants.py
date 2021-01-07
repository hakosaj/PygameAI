
import sys
import os
import random
import time
import pygame
import copy
import math
import concurrent.futures
from pygame.locals import *
from pynput.keyboard import Key, Controller

#Shapes
currentOnes=["z","j","t","o","s","l","i"]

#multiprocessing for individual moves
multi=True

#Screen size
width,height=520,600
size = width,height

#blockid
blockID=1


#Visual or not
visual=False
if visual:
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tetris")

#Starts
ystart=5
xstart=7

#blocksize
blocksize = 20

#Colors
BLACK = 0,0,0
BLUE = 135,206,235
GREEN = 124,252,0
RED = 145,40,60
WHITE = 255,255,255
BROWN = 70,32,32