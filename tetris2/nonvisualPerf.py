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
from keyEvents import *
from aiagent import *

# Profiling
import fileinput
import cProfile

pr = cProfile.Profile()
pr.enable()

weights = [-0.810066, 0.560666, -0.75663, -0.084483]


manual = False
maxreps = 700
reps = 0
GA = False


# AIagent
blocknumber = 0
agent = Aiagent(weights)
individualNumber = 0
gensize = 0
maxBlocks = 0
generation = 0
maxgens = 0


# keyb
# configurations = i j t o s z l
currentOne = random.choice(currentOnes)
offset = 0
currentColor = RED


# loselimit
loselimit = 6

# Tetris grid
gridsizex = 15
gridsizey = 30
g = Grid(gridsizex, gridsizey, loselimit, agent)

# Screen objects
g.createSquares()


# Initialize pygame
# pygame.init()
# pygame.font.init()
# Fonts and gavkground
# scorefont = pygame.font.SysFont('Comic Sans MS',40)
# gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
# weightfont = pygame.font.SysFont('Arial',20)

# start_time = None
# clock = pygame.time.Clock ()
tickcounter = 0


# Block starting point
xCur = xstart
yCur = ystart
createConfiguration(xCur, yCur, offset, g, currentOne)


# score
score = 0

# Lost
lost = False

start = time.time()
while lost == False and reps < maxreps:
    reps += 1

    params = [xCur, yCur, currentOne, currentColor, lost, g, offset]

    xCur, yCur, currentOne, currentColor, lost, g, offset = params

    if tickcounter % 20 == 0:
        params = downKey(xCur, yCur, offset, g, currentOne, currentColor, manual)
        xCur, yCur, currentOne, currentColor, lost, g, offset = params

    score += g.removeFullRows()

    # Take single actions
    if tickcounter % 5 == 0 and yCur > loselimit and not manual:
        action = agent.takeAction()
        if action == 1:
            params = upKey(xCur, yCur, offset, g, currentOne, currentColor)
            xCur, yCur, currentOne, currentColor, lost, g, offset = params
        elif action == 2:
            params = rightKey(xCur, yCur, offset, g, currentOne, currentColor)
            xCur, yCur, currentOne, currentColor, lost, g, offset = params
        elif action == 3:
            params = leftKey(xCur, yCur, offset, g, currentOne, currentColor)
            xCur, yCur, currentOne, currentColor, lost, g, offset = params
        else:
            params = spaceKey(xCur, yCur, offset, g, currentOne, currentColor, manual)
            xCur, yCur, currentOne, currentColor, lost, g, offset = params
            blocknumber += 1
            if blocknumber == maxBlocks:
                lost = True

    tickcounter += 1


print(f"Time: {time.time()-start}")
# Lost game, return score
print(f"Individual: {individualNumber}, fitness: {score}")

pr.disable()
pr.print_stats(sort="cumtime")
