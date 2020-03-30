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


class FlappyQAgent: 

    def __init__(self,discount, qAlpha ):
        #Action=true-matrix
        self.QMatrix = np.zeros((2,580,600,2))#action,y,x,ded
        self.discount = discount
        self.alpha=qAlpha

    def updateQMatrix(self,action,state,value):
        y=state[0]
        x=state[1]
        d=state[2]
        if d:
            self.QMatrix[action,y,x,0]=value
        else:
            self.QMatrix[action,y,x,1]=value





    def getFromQ(self,action,state):
        y=state[0]
        x=state[1]
        d=state[2]

        if d:
            return self.QMatrix.item((action,y,x,0))
        else:
            return self.QMatrix.item((action,y,x,1))
        