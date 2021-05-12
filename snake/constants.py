import sys
import os
import random
import time
import pygame
import math
from pygame.locals import *


# Multiprocessing
multi = True
# Visualization
visualized = False
# Walls
walls = True
# Draw paths
paths = True


# Multiprocessing
multi = True
# Visualization
visualized = False
# Walls
walls = True
# Draw paths
paths = False


# ITers
iterations = 1000

# speed
fps = 500

# prints
prints = False

# prints important
importantPrints = False

# blocksize
blocksize = 20
gridsizex = 20
gridsizey = 20

# Screen size
width, height = blocksize * gridsizey, blocksize * gridsizex
size = width, height

# screen
if visualized:
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake")

# Colors
BLACK = 0, 0, 0
BLUE = 135, 206, 235
GREEN = 124, 252, 0
RED = 255, 0, 0
WHITE = 255, 255, 255
BROWN = 70, 32, 32
YELLOW = 0, 252, 252
