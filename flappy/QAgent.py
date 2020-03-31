import sys
import numpy as np
import os
import random
import time
import pygame
import math
from constants import *
from chromosome import Chromosome
from bird import Bird
from selection import *
from pillar import Pillar
from pygame.locals import *

    #ata = np.zeros((580,600,2))
#y: [-280,300]
#x: [600,0]


class QAgent: 

    def __init__(self,discount ):
        #Action=true-matrix
        self.QMatrix = np.zeros((2,118,600))#action,y,x,ded
        self.discount = discount
        self.stateCount= np.zeros((580,600))

    def updateQMatrix(self,action,state,value):
        y=int(state[0]/5)
        x=state[1]
        self.QMatrix[action,y,x]=value



    def updateStateCount(self,state):
        self.stateCount[state[0],state[1]]+=1
        return self.stateCount[state[0],state[1]]


    def loadMatrix(self, name):
        self.QMatrix=np.load("flappyQData//"+name+".npy")





    def getFromQ(self,action,state):
        y=int(state[0]/5)
        x=state[1]
        return self.QMatrix.item((action,y,x))
        