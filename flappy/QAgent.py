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

# ata = np.zeros((580,600,2))
# y: [-280,300]
# x: [600,0]


"""Agent for the Q-learning flappym with the matrices and matrix updates
"""
class QAgent:
    def __init__(self, discount= 0.9):
        """Initialize matrix

        Args:
            discount (float): discount parameter value
        """
        # Action=true-matrix
        self.QMatrix = np.zeros((2, 118, 600))  # action,y,x,ded
        self.discount = discount
        self.stateCount = np.zeros((580, 600))

    def updateQMatrix(self, action, state, value):
        """Update the q matrix based on the parameters

        Args:
            action (bool): action boolean
            state (list): list depicting the state
            value (float): current state q value
        """
        y = int(state[0] / 5)
        x = state[1]
        self.QMatrix[action, y, x] = value

    def updateStateCount(self, state):
        """Update the times one has been on this state

        Args:
            state (list): list depicting the current state

        Returns:
            int: statecount
        """
        self.stateCount[state[0], state[1]] += 1
        return self.stateCount[state[0], state[1]]

    def loadMatrix(self, name):
        """Load a q-matrix from the file

        Args:
            name (str): filename for the matrix to load to the object
        """
        self.QMatrix = np.load("flappyQData//" + name + ".npy")

    def getFromQ(self, action, state):
        """Get any item from the matrix

        Args:
            action (bool): boolean action
            state (state): state of the game

        Returns:
            list: state
        """
        y = int(state[0] / 5)
        x = state[1]
        return self.QMatrix.item((action, y, x))
