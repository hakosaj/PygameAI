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
from pygame.locals i

    #ata = np.zeros((580,600,2))
#y: [-280,300]
#x: [600,0]

class FlappyQAgent: 

    def __init__(self):
        self.QMatrix = np.zeros((580,600,2))#y,x,ded
        self.rewards = np.ndarray(15,-1000)#alive,dead
        self.discount = 1
        