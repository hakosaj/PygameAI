import pygame
import sys
import os
import random
import time
import pygame


tolerance=30

#Screen size
width,height=700,480
size = 1000,height

agentsc=60

#Constants
ground=40
pillar=100
gap=100

pillarFrequency =1.8
basePillarFrequency=pillarFrequency

pillargapL=-60
pillargapU= 100

survivalRate=0.25

currentGeneration=0


#Colors
BLACK = 0,0,0
BLUE = 135,206,235
GREEN = 124,252,0
RED = 145,40,60
LIGHTGRAY = 155,155,155
WHITE = 255,255,255


#Screen objects
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Demo")


#Bird Movement
x,y = 100,150
right = 1
left = 2
direction =0
size=[30,30]
velocity=0
acc=-0.4
bump = 6



#Pillar movement
pillarVelocity=5
pillarpos=width

#Ticks and time and score
tickc=0
keytick=0
score=0
difficultyTick=0




#Object specifics

groundcolor=GREEN
