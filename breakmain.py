import sys
import os
import random
import time
import pygame
import math
from pygame.locals import *
from pynput.keyboard import Key, Controller
from breakconstants import *
from block import Block
from paddle import Paddle





#Initialize pygame
pygame.init()
pygame.font.init()
#Fonts and gavkground
scorefont = pygame.font.SysFont('Comic Sans MS',40)
gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
algofont = pygame.font.SysFont('Arial',20)

paddle =Paddle()
blocks=[]

for row in range(0,blocksY):
    for col in range(0,blocksX):
        blocks.append(Block(leftMargin+col*blockX,upMargin+row*blockY)) 



start_time = None
clock = pygame.time.Clock ()


while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                pygame.event.clear()
                event = pygame.event.wait()
                while (event.key!=pygame.K_o):
                    pygame.event.clear()
                    event = pygame.event.wait()                    

            if event.key == pygame.K_SPACE:
               ata=2 
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    screen.fill(BROWN)
    for block in blocks:
        block.draw_block()


        #draw info
        #screen.blit(datasurface,(750,10))
        #datasurface=algofont.render("Avg fit: "+str(avgfitness),False,(0,0,0))
        #screen.blit(datasurface,(750,30))
        #datasurface=algofont.render("Generation: "+str(currentGeneration),False,(0,0,0))
        #screen.blit(datasurface,(750,50))
        #datasurface=algofont.render("Alive: "+str(agentsc-deadcount)+"/"+str(agentsc),False,(0,0,0))
        #screen.blit(datasurface,(750,70))


    pygame.display.flip()
    clock.tick(30)




