import sys
import os
import random
import time
import pygame
import math
from block import Block
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller
from grid import *
from configurations import *


#configurations = i j t o s z l
currentOnes=["z","j","t","o","s","l"]
currentOne=random.choice(currentOnes)
offset=0
currentColor=RED


#loselimit
loselimit = 6

#Tetris grid
gridsizex=15
gridsizey=30
g = Grid(gridsizex,gridsizey,loselimit)

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
                if (currentOne=="l"):
                    if not ((offset==2 and xCur>12) or (offset==6 and xCur>13) ):
                        if createConfiguration(xCur,yCur,offset+2,g,currentOne):
                            offset+=2
                        else:
                            createConfiguration(xCur,yCur,offset,g,currentOne)

                else:
                    if (currentOne!="o"):
                        if createConfiguration(xCur,yCur,offset+2,g,currentOne):
                            offset+=2
                        else:
                            createConfiguration(xCur,yCur,offset,g,currentOne)

            
            elif event.key == pygame.K_RIGHT:
                if createConfiguration(xCur+1,yCur,offset,g,currentOne):
                    xCur+=1
                else:
                    createConfiguration(xCur,yCur,offset,g,currentOne)


            elif event.key == pygame.K_DOWN:
                if createConfiguration(xCur,yCur+1,offset,g,currentOne):
                    yCur+=1
                else:
                    xCur,yCur, currentOne, currentColor,lost =g.spawnBlock(xCur,yCur,offset,g,currentOne,currentColor,currentOnes)

            elif event.key == pygame.K_SPACE:
                while createConfiguration(xCur,yCur+1,offset,g,currentOne):
                    yCur+=1
                xCur,yCur, currentOne, currentColor, lost =g.spawnBlock(xCur,yCur,offset,g,currentOne,currentColor,currentOnes)
                

            elif event.key == pygame.K_LEFT:
                if createConfiguration(xCur-1,yCur,offset,g,currentOne):
                    xCur-=1
                else:
                    createConfiguration(xCur,yCur,offset,g,currentOne)


            elif event.key == pygame.K_r:
                g.printGrid()


    g.drawGrid(currentColor)

    if (tickcounter%20==0):
        if createConfiguration(xCur,yCur+1,offset,g,currentOne):
            yCur+=1
        else:
            xCur,yCur, currentOne, currentColor, lost =g.spawnBlock(xCur,yCur,offset,g,currentOne,currentColor,currentOnes)



    score+=g.removeFullRows()
    scorestring = "Score: "+ str(score)
    textsurface = scorefont.render(scorestring,False,(252,0,0))
    screen.blit(textsurface,(320,20))


    if lost:
        print(f"Lovea! Your score was {score}!")
        pygame.quit()
        sys.exit()





    tickcounter+=1
    pygame.display.flip()
    clock.tick(50)




