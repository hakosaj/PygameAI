import sys
import numpy as np
import os
import random
import time
import pygame
import math
from flappyConstants import *
from chromosome import Chromosome
from bird import Bird
from selection import *
from pillar import Pillar
from pygame.locals import *

    #ata = np.zeros((580,600,2))
#y: [-280,300]
#x: [600,0]

rewardDead=-1000
rewardAlive=15

class FlappyQAgent: 

    def __init__(self,discount):
        self.QMatrix = np.zeros((580,600,2))#y,x,ded
        self.discount = discount


    def getAction(self,y,x,d):
        if d:
            return self.QMatrix.item((y,x,0))
        else:
            return self.QMatrix.item((y,x,1))
        