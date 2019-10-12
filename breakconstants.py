import pygame
import sys
import os
import random
import time
import pygame


#Ball dims
ballRadius=8
ballVelocity=3
paddleVelocityModifier=30
startX=200
startY=300

#Game dimensions
rightMargin=50
leftMargin=50
upMargin=50
lowMargin=300

#Random modifiers
paddleBounceModifier=8
blockBounceModifier=4

#Blocks size, blocksize and ordering
blocksX=9
blocksY=5

blockX=80
blockY=35

#Screen size
width,height=800,700
size = width,height


#Constants
paddlewidth=2*blockX
paddleSpeed=10
mutationRate=0.9
survivalRate=0.2

currentGeneration=0


#Colors
BLACK = 0,0,0
BLUE = 135,206,235
GREEN = 124,252,0
RED = 145,40,60
WHITE = 255,255,255
BROWN = 70,32,32


#Screen objects
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Demo")


#Bird Movement
x,y = 100,80
right = 1
left = 2
direction =0
size=[30,30]
velocity=0
acc=-0.4
bump = 6




#Ticks and time and score
tickc=0
keytick=0
score=0
difficultyTick=0
#Object specifics

groundcolor=GREEN
