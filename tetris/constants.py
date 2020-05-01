
import sys
import os
import random
import time
import pygame
import math
from pygame.locals import *
from pynput.keyboard import Key, Controller



#Screen size
width,height=300,600
size = width,height

#blockid
blockID=1

#screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")


#blocksize
blocksize = 20

#Colors
BLACK = 0,0,0
BLUE = 135,206,235
GREEN = 124,252,0
RED = 145,40,60
WHITE = 255,255,255
BROWN = 70,32,32