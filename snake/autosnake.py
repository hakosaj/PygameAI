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
from agenttools import bfs, takeAction
import cProfile


def game(t=2):

    #Tetris grid, true as last argument if walls
    g = Grid(gridsizex,gridsizey,walls)

    #Screen objects
    g.createSquares()
    snek = Snek(5,5,g)
    g.randomFood()


    score=0
    #Initialize pygame
    if visualized:
        pygame.init()
        pygame.font.init()
        #Fonts and gavkground
        scorefont = pygame.font.SysFont('Comic Sans MS',40)
        gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
        algofont = pygame.font.SysFont('Arial',20)

    orientations=[]





    start_time = None
    clock = pygame.time.Clock ()

    foodEaten=True

    tickcounter=0





    while not snek.dead:
        if visualized:
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



        if foodEaten:
            orientations=bfs(g,snek)
            foodEaten=False

        if len(orientations)>0:
            orientations=takeAction(orientations,snek)


        if snek.moveSnake():
            foodEaten=True
            score+=1

        if visualized:
            g.drawGrid()

        





                


        tickcounter+=1
        if visualized:
            pygame.display.flip()
            clock.tick(fps)


    print(f"Score: {score}")
    return score

game()