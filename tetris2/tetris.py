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



def game(weights,individualNumber,gensize,maxBlocks,generation, maxgens, manualc,GA):
    

    #AIagent
    blocknumber=0
    manual=manualc
    agent=Aiagent(weights)
    if manual:
        individualNumber=0
        gensize=0
        maxBlocks=0
        generation=0
        maxgens=0


    #keyb
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
    weightfont = pygame.font.SysFont('Arial',20)

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

    while lost==False:

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
                    params= downKey(xCur,yCur,offset,g,currentOne,currentColor,manual)

                elif event.key == pygame.K_SPACE:
                    params= spaceKey(xCur,yCur,offset,g,currentOne,currentColor,manual)

                elif event.key == pygame.K_r:
                    g.printGrid()
        
        xCur,yCur,currentOne,currentColor,lost,g,offset=params

        g.drawGrid(currentColor)

        if (tickcounter%20==0):
            params=downKey(xCur,yCur,offset,g,currentOne,currentColor,manual)
            xCur,yCur,currentOne,currentColor,lost,g,offset=params


        score+=g.removeFullRows()


        #
        scorestring = "Score: "+ str(score)
        textsurface = scorefont.render(scorestring,False,(252,0,0))
        screen.blit(textsurface,(310,20))


        if not manual:
            if GA:
                weightstring = "Individual "+str(individualNumber+1)+"/"+str(gensize)
                weighttext = weightfont.render(weightstring,False,(252,0,0))
                screen.blit(weighttext,(310,60))

                blockstring = "Blocks "+str(blocknumber)+"/"+str(maxBlocks)
                blocktext = weightfont.render(blockstring,False,(252,0,0))
                screen.blit(blocktext,(310,90))


                genstring = "Current gen "+str(generation+1)+"/"+str(maxgens+1)
                gentext = weightfont.render(genstring,False,(252,0,0))
                screen.blit(gentext,(310,120))

            weightstring = "Weight a: "+ str(round(weights[0],3))
            weighttext = weightfont.render(weightstring,False,(252,0,0))
            screen.blit(weighttext,(310,150))

            weightstring = "Weight b: "+ str(round(weights[1],3))
            weighttext = weightfont.render(weightstring,False,(252,0,0))
            screen.blit(weighttext,(310,180))

            weightstring = "Weight c: "+ str(round(weights[2],3))
            weighttext = weightfont.render(weightstring,False,(252,0,0))
            screen.blit(weighttext,(310,210))

            weightstring = "Weight d: "+ str(round(weights[3],3))
            weighttext = weightfont.render(weightstring,False,(252,0,0))
            screen.blit(weighttext,(310,240))

            weightstring = "a: totalHeight"
            weighttext = weightfont.render(weightstring,False,(252,0,0))
            screen.blit(weighttext,(310,270))

            weightstring = "b: linesToClear"
            weighttext = weightfont.render(weightstring,False,(252,0,0))
            screen.blit(weighttext,(310,300))

            weightstring = "c: holes"
            weighttext = weightfont.render(weightstring,False,(252,0,0))
            screen.blit(weighttext,(310,330))

            weightstring = "d: bumpiness"
            weighttext = weightfont.render(weightstring,False,(252,0,0))
            screen.blit(weighttext,(310,360))


        #Take single actions
        if tickcounter%2==0 and yCur>loselimit and not manual:
        #if yCur>loselimit and not manual:
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
                params=spaceKey(xCur,yCur,offset,g,currentOne,currentColor,manual)
                xCur,yCur,currentOne,currentColor,lost,g,offset=params
                blocknumber+=1
                if blocknumber==maxBlocks:
                    lost=True







        tickcounter+=1
        pygame.display.flip()
        if (manual):
            clock.tick(100)
        else:
            clock.tick(200)
    

    #Lost game, return score
    print(f"Individual: {individualNumber}, fitness: {score}")
    return score

def main():
    preweights=[
    -0.88548,
     1.33299,
    -1.37767,
    -0.241657
    ]
    if len(sys.argv)>1:
        if str(sys.argv[1])=='manual':
            game([0,0,0,0],0,0,0,0,0,True,False)
        elif str(sys.argv[1])=='auto':
            game(preweights,0,0,0,0,0,False,False)
    else:
        print("No control argument given")
main()
