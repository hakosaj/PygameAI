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
    fitSum=sum(scores)
    scores=list(map(lambda x:x/fitSum,scores))

    cumulativeP=[]
    currentSum=0
    for s in scores:
        currentSum+=s
        cumulativeP.append(currentSum)

    chosenIndexes=[]
    survivorCount=int(math.ceil(agentsc/4))
    for a in range(survivorCount):
        draw = random.random()
        for i in range(len(cumulativeP)):
            if cumulativeP[i]>draw:
                if i not in chosenIndexes:
                    chosenIndexes.append(i)
                    break


    survivors=[]
    for item in chosenIndexes:
        survivors.append(best[item] )
    return survivors,survivorCount