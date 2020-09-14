import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller
from grid import *
from configurations import * 
from keyEvents import *
from aiagent import *




#AIagent
agent=Aiagent()

#keyb
keyboard=Controller()
#configurations = i j t o s z l
currentOne=random.choice(currentOnes)
offset=0
currentColor=RED


#loselimit
loselimit = 6

#Tetris grid
gridsizex=15
gridsizey=30
g = Grid(gridsizex,gridsizey,loselimit,agent)

#Screen objects
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


#Block starting point
xCur=xstart
yCur=ystart
createConfiguration(xCur,yCur,offset,g,currentOne)


#score
score=0

#Lost
lost=False

while True:

    params=[xCur,yCur,currentOne,currentColor,lost,g,offset]

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
            elif event.key == pygame.K_UP:
                params= upKey(xCur,yCur,offset,g,currentOne,currentColor)
            
            elif event.key == pygame.K_RIGHT:
                params= rightKey(xCur,yCur,offset,g,currentOne,currentColor)

            elif event.key == pygame.K_LEFT:
                params=leftKey(xCur,yCur,offset,g,currentOne,currentColor)

            elif event.key == pygame.K_DOWN:
                params= downKey(xCur,yCur,offset,g,currentOne,currentColor)

            elif event.key == pygame.K_SPACE:
                params= spaceKey(xCur,yCur,offset,g,currentOne,currentColor)

            elif event.key == pygame.K_r:
                g.printGrid()
    
    xCur,yCur,currentOne,currentColor,lost,g,offset=params

    g.drawGrid(currentColor)

    if (tickcounter%20==0):
        params=downKey(xCur,yCur,offset,g,currentOne,currentColor)
        xCur,yCur,currentOne,currentColor,lost,g,offset=params


    score+=g.removeFullRows()
    scorestring = "Score: "+ str(score)
    textsurface = scorefont.render(scorestring,False,(252,0,0))
    screen.blit(textsurface,(320,20))


    if lost:
        print(f"Lovea! Your score was {score}!")
        pygame.quit()
        sys.exit()


    #Take single actions
    if tickcounter%5==0 and yCur>loselimit:
        action=agent.takeAction()
        if action==1:
            params=upKey(xCur,yCur,offset,g,currentOne,currentColor)
            xCur,yCur,currentOne,currentColor,lost,g,offset=params
        elif action==2:
            params=rightKey(xCur,yCur,offset,g,currentOne,currentColor)
            xCur,yCur,currentOne,currentColor,lost,g,offset=params
        elif action==3:
            params=leftKey(xCur,yCur,offset,g,currentOne,currentColor)
            xCur,yCur,currentOne,currentColor,lost,g,offset=params
        else:
            params=spaceKey(xCur,yCur,offset,g,currentOne,currentColor)
            xCur,yCur,currentOne,currentColor,lost,g,offset=params







    tickcounter+=1
    pygame.display.flip()
    clock.tick(200)




