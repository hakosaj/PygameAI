import sys
import os
import random
import time
import pygame
import numpy as np
import math
from constants import *
from chromosome import Chromosome
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


#Algos:0 is normal game, 1 is GA
chosenAlgo=1
print("Chosen algorithm: GA")
birds=[]


for a in range(agentsc):
    birds.append(Bird())
    birds[a].col=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

agents=[]

for a in range(agentsc):
    agents.append(Chromosome())
    agents[a].randoms(
    )
    
topfitness=0
avgfitness=0
prevAvg2=0
generation = []
prevAvg=0



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
    for a in range(agentsc):
        if agents[a].dead==False:
            
            birds[a].draw_bird()

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









    #Check collision
    for i in range(agentsc):
        for pillar in pillars:
            if ( agents[i].dead==False and birds[i].rect.colliderect(pillar.upperPillar) or birds[i].rect.colliderect(pillar.lowerPillar)):
                agents[i].setEndScore(score)
                agents[i].dead=True
                generation.append(agents[i])
                
    deadcount=0
    for i in range(agentsc):
        if agents[i].dead:
            deadcount+=1


    topIndividuals=[]
    for i in range(10):
        topIndividuals.append(Chromosome)



    if deadcount==len(agents):
        currentGeneration+=1
        score=0
        tickc=0
        keytick=0
        score=0
        difficultyTick=0
        pillarVelocity=5
        pillarFrequency=basePillarFrequency
        birds[0].y=y+(random.randint(-200,100))
        pillars.clear()
        p=Pillar(width-50)
        pillars.append(p)

        best=sorted(agents,key=lambda x: x.endScore,reverse=True)
        scores=list(map(lambda x: x.endScore-200,best))
        bestest=best[0]
        bestest2=best[1]


        prevAvg=avgfitness
        for item in best:
            avgfitness+=item.endScore
        avgfitness=avgfitness/(agentsc*1.0)
        if topfitness<best[0].endScore:
            topfitness=best[0].endScore


        #Selection
        #survivors,survivorCount=elitism(best)

        survivors,survivorCount=roulette(scores,best)


        #Generate parent pairs
        parentPairs=[]
        while(len(parentPairs)<agentsc):

            pair1=random.randint(0,survivorCount-1)
            pair2=random.randint(0,survivorCount-1)

            if (pair1!=pair2):
                p=(pair1,pair2)
                parentPairs.append(p)

        agents[0]=bestest
        agents[1]=bestest2


        #Crossover
        for i in range(0,agentsc):
            pair=parentPairs[i]
            agents[i]=Chromosome()

            qualities=[0,1,2,3]

            while len(qualities)!=0:  
                chosenQuality=random.randint(0,3)
                whichParent=random.randint(0,1)
                if chosenQuality in qualities:
                    qualities.remove(chosenQuality)
                    try:

                        if chosenQuality==1:
                            agents[i].velocityLimitLow=survivors[pair[whichParent]].velocityLimitLow
                        elif chosenQuality==2:
                            agents[i].velocityLimitUp=survivors[pair[whichParent]].velocityLimitUp
                        elif chosenQuality==3:
                            agents[i].xDistUp=survivors[pair[whichParent]].xDistUp
                        else:
                            agents[i].yDistUp=survivors[pair[whichParent]].yDistUp
                    except IndexError:
                        print("i: "+str(i))
                        print("whichparent: "+str(whichParent))
                        print("pair: ",pair)



            #Mutate
            if (avgfitness>300 and avgfitness <1000):
                if (random.random()>0.8):
                    agents[i].mutate(20)
                else:
                    agents[i].mutate(0.5)
            elif (avgfitness> 1000):
                if (random.random()>0.8):
                    agents[i].mutate(10)
                else:
                    agents[i].mutate(0.2)

            else:
                agents[i].reset()
                agents[i].randoms()


                #else:
                #   pygame.quit()
                #  sys.exit()
    
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


    distx=str(agents[0].xDistUp)
    disty=str(agents[0].yDistUp)
    vell=str(agents[0].velocityLimitLow)
    velu=str(agents[0].velocityLimitUp)
    individual=str(len(generation)+1)

    datasurface=algofont.render("Best ind: "+str(topfitness),False,(0,0,0))
    screen.blit(datasurface,(750,10))
    datasurface=algofont.render("Avg fit: "+str(avgfitness),False,(0,0,0))
    screen.blit(datasurface,(750,30))
    datasurface=algofont.render("Generation: "+str(currentGeneration),False,(0,0,0))
    screen.blit(datasurface,(750,50))
    datasurface=algofont.render("Alive: "+str(agentsc-deadcount)+"/"+str(agentsc),False,(0,0,0))
    screen.blit(datasurface,(750,70))





    pygame.display.flip()
    

    
    harder=False
    if harder:
        if score%100==0:
            pillarVelocity+=0.05
        
        if score%2000==0:
            pillarFrequency+=1

    for a in range(len(agents)):
        agents[a].decide(birds[a],pillars)
    



    clock.tick(60)




