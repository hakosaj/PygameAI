import sys
import os
import random
import time
import pygame
import math
from snek import Snek
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller
from grid import *



#Tetris grid
gridsizex=20
gridsizey=20
g = Grid(gridsizex,gridsizey)

#Screen objects
g.createSquares()
snek = Snek(5,5,g)




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
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            elif event.key == pygame.K_RIGHT:
                snek.changeOrientation(2)
            elif event.key == pygame.K_DOWN:
                snek.changeOrientation(4)
            elif event.key == pygame.K_LEFT:
                snek.changeOrientation(6)
            elif event.key == pygame.K_UP:
                snek.changeOrientation(0)

            elif event.key == pygame.K_r:
                g.printGrid()


    g.drawGrid()

    snek.moveSnake()
    snek.drawSnake()


            


    tickcounter+=1
    pygame.display.flip()
    clock.tick(5)




