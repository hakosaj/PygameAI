import sys
import os
import random
import time
import pygame
import math
from constants import *
from chromosome import Chromosome
from bird import Bird
from pillar import Pillar
from pygame.locals import *


def roulette(scores, best):
    """Roulette selection for the GA

    Args:
        scores (list[int]): list of fitness values
        best (int): best fitness value

    Returns:
        list[int], int: survivor indices as list, survivor count
    """
    scores = list(map(lambda x: x ** 2 / sum(scores), scores))
    cumulativeP = []
    currentSum = 0
    for s in scores:
        currentSum += s
        cumulativeP.append(currentSum)

    chosenIndexes = []
    survivorCount = int(math.ceil(agentsc * survivalRate))
    for a in range(survivorCount):
        draw = random.random()
        for i in range(len(cumulativeP)):
            if cumulativeP[i] > draw:
                chosenIndexes.append(i)
                break

    survivors = []
    for item in chosenIndexes:
        survivors.append(best[item])
    return survivors, survivorCount


def elitism(best):
    """Strict elitism selection, get the best performing individuals

    Args:
        best (list[list[float]]): list of the best  individuals

    Returns:
        list[list[float]], int: list of the chosen individuals, amount of individuals
    """
    survivorCount = int(math.ceil(agentsc * survivalRate))

    survivors = []
    for i in range(survivorCount):
        survivors.append(best[i])
    return survivors, survivorCount
