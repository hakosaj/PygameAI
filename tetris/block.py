
import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller


rcti = pygame.Rect(101,101,9,9)
rcto = pygame.Rect(100,100,10,10)

#configurations = i j l o s z t

class Block:

    def __init__(self,location,configuration):
        self.x=location[0]
        self.y=location[1]
        self.configuration = configuration
        self.rectangles=createConfiguration(configuration)


    def createConfiguration(self,configuration):
        



