import sys
import os
import random
import time
import pygame
import math
from constants import *
from tetris import *


#Population size
popsize=5
a=-2
b=2
fittestIndividuals=10

        #ax = self.a*g.totalHeight()
        #bx = self.b*g.virtualFullRows()
        #cx = self.c*g.holes()
        #dx = self.d*g.bumpiness()


#Initialize generation
parents=[]
for i in range(popsize):
    parents.append([random.uniform(a, b),random.uniform(a, b),random.uniform(a, b),random.uniform(a, b)])


#Fitness test: play the game
fitnesses=[]
for i in range(len(parents)):
    fitness=game(parents[i],i,popsize)
    fitnesses.append((i,fitness))

for item in fitnesses:
    print(item)
