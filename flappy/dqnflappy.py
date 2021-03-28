import sys
import os
import random
import time
import pygame
import numpy as np
import math
from constants import *
from QAgent import QAgent
from bird import Bird
from selection import *
from pillar import Pillar
from pygame.locals import *
from pynput.keyboard import Key, Controller


snapshotCounter=0
rewardPass=5
rewardDie=-1
gamma=0.9
frames=20

#Initialize pygame
pygame.init()
pygame.font.init()
#Fonts and gavkground
scorefont = pygame.font.SysFont('Comic Sans MS',40)
gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
algofont = pygame.font.SysFont('Arial',20)

#Image memory
image_memory=np.zeros((frames,96,140))
picmemory = []

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


#Algos:0 is normal game, 1 is GA
print("Chosen algorithm: CNN-DQN")
chosenAlgo=2
dead=False
discount=1
qAgent = QAgent(discount)
if (len(sys.argv)==3):
    qAgent.loadMatrix(sys.argv[2])
actionTaken=False
previousAction=0
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










    collide=False
    for pillar in pillars:
        if (birds[0].rect.colliderect(pillar.upperPillar) or birds[0].rect.colliderect(pillar.lowerPillar)):
            collide=True


    if collide:
        birds[0].dead=True
        score=0
        tickc=0
        keytick=0
        bird.velocity=0
        score=0
        difficultyTick=0
        pillarVelocity=5
        pillarFrequency=basePillarFrequency
        birds[0].y=y+(random.randint(-100,200))
        #birds[0].y=y
        pillars.clear()
        p=Pillar(width-150)
        pillars.append(p) 

    else:
        birds[0].dead=False

            
                
        

    score+=2
    scorestring = "Score: "+ str(score)
    textsurface = scorefont.render(scorestring,False,(200,130,200))
    screen.blit(textsurface,(750,20))


    try:
        nextPillar = next(x for x in pillars if x.pos>bird.x)
        speedstring = "Xdist: "+ str(int(nextPillar.pos-birds[0].x))
        speedstring2 = "Ydist:" + str(int(nextPillar.gap+gap/2-birds[0].y))
        textsurface2 = scorefont.render(speedstring,False,(200,130,200))
        textsurface3 = scorefont.render(speedstring2,False,(200,130,200))
        screen.blit(textsurface2,(750,60))
        screen.blit(textsurface3,(750,90))
    except StopIteration:
        pass




    pygame.display.flip()
    

    
    harder=False
    if harder:
        if score%100==0:
            pillarVelocity+=0.05
        
        if score%2000==0:
            pillarFrequency+=1
    







    #Image treatment and memory
    scaledsurface =pygame.transform.scale(screen.subsurface(0,0,width,height-ground),(int(width/5),int(height/5)))
    scaled=pygame.surfarray.array2d(scaledsurface).swapaxes(0,1)
    scal=list(map(lambda x: (100*x/16777215),scaled))
    snapshot=np.array(scal)

    #shape: 96,140

    image_memory = np.roll(image_memory, 1, axis = 0)
    image_memory[0,:,:] = snapshot

    #http://cs231n.stanford.edu/reports/2016/pdfs/111_Report.pdf
    #https://medium.com/analytics-vidhya/deep-q-network-with-convolutional-neural-networks-c761697897df
    #https://cse.iitkgp.ac.in/~sudeshna/courses/DL18/CNN-DeepQ-8Mar-2018.pdf
    #https://www.datahubbs.com/deepmind-dqn/


    #Frame memory. Picture form!
    if len(picmemory)!=frames:
        scaledsurface =pygame.transform.scale(screen.subsurface(0,0,width,height-ground),(int(width/5),int(height/5)))
        scaled=pygame.surfarray.array2d(scaledsurface).swapaxes(0,1)
        picmemory.append(scaledsurface)
    #Picmemory: Newest always in the end. End intensity max, reduce while index drops
    if len(picmemory)==frames:
        pygame.image.save(picmemory[0],'snapshot.png')
        merged=picmemory[0].copy()
        for i in range(len(picmemory)):
            ata = picmemory[i]
            ata.set_alpha(min(255,i*15))
            merged.blit(ata,(0,0))
            fname=f"pic{i}.png"
            pygame.image.save(ata,fname)
        pygame.image.save(merged,'merged.png')
        picmemory=picmemory[1:]
        tha
        #print(len(picmemory))




    clock.tick(60)

    snapshotCounter+=1
    if snapshotCounter==frames:
        snapshotCounter=0




