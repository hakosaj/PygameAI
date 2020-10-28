
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

#speed
fps=20

#prints
prints=False

#prints important
importantPrints=False

#blocksize
blocksize = 25
gridsizex=25
gridsizey=25

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