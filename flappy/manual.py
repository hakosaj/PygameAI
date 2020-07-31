import sys
import os
import random
import time
import pygame
import numpy as np
import math
from constants import *
from chromosome import Chromosome
from QAgent import QAgent
from bird import Bird
from selection import *
from pillar import Pillar
from pygame.locals import *
from pynput.keyboard import Key, Controller


#Seuraavaksi:
#Erittele filuihin
#Päätä: minkälaista AI? geneettinen, neuro with backprop, Q-learning, NEAT
#pelaamisesta oppiva


#Initialize pygame
pygame.init()
pygame.font.init()
#Fonts and gavkground
scorefont = pygame.font.SysFont('Comic Sans MS',40)
gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
algofont = pygame.font.SysFont('Arial',20)
bg = pygame.image.load("clouds.png")



start_time = None
clock = pygame.time.Clock ()

#Mitä arvotaan: 
#kuinka kauan ennen painetaan up, x-suunta
#kuinka monta kertaa painataan up, y-suunta
#mikä on rajanopeus
pillars =[]
p=Pillar(width-150)
pillars.append(p) 
harder=True
iterations=0


chosenAlgo=0
birds=[]



agentsc=1
birds.append(Bird())


while True:

    
    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                pygame.event.clear()
                event = pygame.event.wait()
                while (event.key!=pygame.K_p):
                    pygame.event.clear()
                    event = pygame.event.wait()                    

            if event.key == pygame.K_SPACE:
                birds[0].bump()

            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    #Bird movement
    for bird in birds:
        bird.velocity +=acc


        bird.y=bird.y-bird.velocity
        if (bird.velocity>10):
            bird.velocity=10

        if (bird.y>height-ground-40):
            bird.y=height-ground-size[1]

        if (bird.y<0):
            bird.y=0



    #draw static
    screen.fill(WHITE)
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,groundcolor,pygame.Rect(0,height-ground,width,ground))
    pygame.draw.rect(screen,BLACK,pygame.Rect(width,0,5,height))



    #birb
    birds[0].draw_bird()

    #pillar

    tickc+=1
    if (tickc ==int(round(width/(5*pillarFrequency)))):
        pillars.append(Pillar(width-50))
        tickc=0

    for pillar in pillars:
        pillar.move_pillar()
        pillar.draw_pillar()
        if (pillar.pos <-600):
            pillars.remove(pillar)








        
    else:
        collide=False
        for pillar in pillars:
            if (birds[0].rect.colliderect(pillar.upperPillar) or birds[0].rect.colliderect(pillar.lowerPillar)):
                collide=True
            if collide:
                score=0
                tickc=0
                keytick=0
                bird.velocity=0
                score=0
                difficultyTick=0
                pillarVelocity=5
                pillarFrequency=basePillarFrequency
                birds[0].y=y
                pillars.clear()
                p=Pillar(width-50)
                pillars.append(p)
    #Texts


    score+=2
    scorestring = "Score: "+ str(score)
    textsurface = scorefont.render(scorestring,False,(200,130,200))
    screen.blit(textsurface,(20,20))


    try:
        nextPillar = next(x for x in pillars if x.pos>bird.x)
        speedstring = "Xdist: "+ str(int(nextPillar.pos-birds[0].x))
        speedstring2 = "Ydist:" + str(int(nextPillar.gap+gap/2-birds[0].y))
        textsurface2 = scorefont.render(speedstring,False,(200,130,200))
        textsurface3 = scorefont.render(speedstring2,False,(200,130,200))
        screen.blit(textsurface2,(20,60))
        screen.blit(textsurface3,(20,90))
    except StopIteration:
        pass



    pygame.display.flip()
    

    
    harder=False
    if harder:
        if score%100==0:
            pillarVelocity+=0.05
        
        if score%2000==0:
            pillarFrequency+=1



    clock.tick(60)




