
import sys
import os
import random
import time
import pygame
import math
from pygame.locals import *
from pynput.keyboard import Key, Controller




#Multiprocessing
multi=False
#Visualization
visualized=True
#Walls
walls=True
#Draw paths
paths=True

#speed
fps=100

#prints
prints=False

#prints important
importantPrints=True

#blocksize
blocksize = 20
gridsizex=30
gridsizey=30

#Screen size
width,height=blocksize*gridsizey,blocksize*gridsizex
size = width,height

#screen
if visualized:
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake")

#Colors
BLACK = 0,0,0
BLUE = 135,206,235
GREEN = 124,252,0
RED = 255,0,0
WHITE = 255,255,255
BROWN = 70,32,32
YELLOW = 0,252,252