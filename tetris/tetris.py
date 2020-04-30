import sys
import os
import random
import time
import pygame
import math
from grid import Grid
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller




def sign(a):
    if a>0:
        return 1
    else:
        return -1




#Constants




#Screen objects
pygame.display.set_caption("Tetris")
g = Grid(15,30)
g.createSquares()


#Initialize pygame
pygame.init()
pygame.font.init()
#Fonts and gavkground
scorefont = pygame.font.SysFont('Comic Sans MS',40)
gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
algofont = pygame.font.SysFont('Arial',20)







start_time = None
clock = pygame.time.Clock ()


tickcounter=0




while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                pygame.event.clear()
                event = pygame.event.wait()
                while (event.key!=pygame.K_o):
                    pygame.event.clear()
                    event = pygame.event.wait()                    
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()




    g.drawGrid()
    tickcounter+=1
    pygame.display.flip()
    clock.tick(30)




