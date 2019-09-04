import sys
import os
import random
import time
import pygame
import math
from flappyConstants import *
from chromosome import Chromosome
from bird import Bird
from pillar import Pillar
from pygame.locals import *
        
        
def roulette(scores,best):
    scores=list(map(lambda x:x^2,scores))
    fitSum=sum(scores)
    scores=list(map(lambda x:x/fitSum,scores))
    cumulativeP=[]
    currentSum=0
    for s in scores:
        currentSum+=s
        cumulativeP.append(currentSum)

    chosenIndexes=[]
    survivorCount=int(math.ceil(agentsc*survivalRate))
    for a in range(survivorCount):
        draw = random.random()
        for i in range(len(cumulativeP)):
            if cumulativeP[i]>draw:
                chosenIndexes.append(i)
                break

    survivors=[]
    for item in chosenIndexes:
        survivors.append(best[item] )
    return survivors,survivorCount




def elitism(best):
    #survivorCount=int(math.ceil(agentsc*survivalRate/2))
    survivorCount=3

    survivors=[]
    for i in range(survivorCount):
        survivors.append(best[i])
    return survivors,survivorCount