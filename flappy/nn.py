import sys
import numpy as np
import os
import random
import time
import pygame
import math


#Defining a 2-layer perceptron with a 4-cell second layer. For now, the net is zerobiased.
#Using four inputs: y-distance from upper pipe, y-distance from lower pipe,
# x-dist from the pipe midpoint, and current velocity
class NN: 

    def __init__(self,x,y):

        #Input vector
        self.input    = x
        
        #First weights, eg. connections from the input layer to the first layer. 
        self.weights1 = np.random.rand(self.input.shape[1],4)

        #Weights from the first hidden layer to output layer
        self.weights2 = np.random.rand(4,1)

        
        self.y        = y
        self.output   = np.zeros(self.y.shape)


    def feedForward(self):
        self.layer1 = sigmoid(np.dot(self.input,self.weights1))
        self.output = sigmoid(np.dot(self.layer1,self.weights2))


    #We shall use the euclidean distance from pipe, both upper and lower one (x-midpoint), as the
    #loss function that shall be minimised.


    def backprop(self):
        