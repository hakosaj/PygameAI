import sys
import os
import random
import time
import pygame
from flappyConstants import *
from chromosome import Chromosome
from bird import Bird
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
p=Pillar(width-50)
pillars.append(p) 

birds=[]
for a in range(agentsc):
    birds.append(Bird())
    birds[a].col=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

agents=[]

for a in range(agentsc):
    agents.append(Chromosome())
    agents[a].randoms()


topfitness=0
harder=False
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
                while (event.key!=pygame.K_o):
                    pygame.event.clear()
                    event = pygame.event.wait()                    

            if event.key == pygame.K_SPACE:
                bird.bump()

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
        mutationRate-=0.2
        time.sleep(1)
        score=0
        tickc=0
        keytick=0
        score=0
        difficultyTick=0
        pillarVelocity=5
        pillarFrequency=basePillarFrequency
        birds[i].y=y
        pillars.clear()
        p=Pillar(width-50)
        pillars.append(p)

        best=sorted(agents,key=lambda x: x.endScore,reverse=True)

        prevAvg=avgfitness
        for item in best:
            avgfitness+=item.endScore
        avgfitness=avgfitness/(40.0)
        if topfitness<best[0].endScore:
             topfitness=best[0].endScore


        #Selection
        for i in range(4):
            topIndividuals[i]=best[i]

        if prevAvg>=avgfitness-tolerance: 
            mutationRate+=0.8



        #Choose the 4 qualities from the five top individuals
        #Crossover
        for i in range(len(agents)):
            agents[i]=Chromosome()

            qualities=[0,1,2,3]
            inds=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4,5,5,6]
            while len(qualities)!=0:        
                chosenInd=random.randint(0,32)
                chosenInd=inds[chosenInd]
                chosenQuality=random.randint(0,3)
                if chosenQuality in qualities:
                    qualities.remove(chosenQuality)

                    if chosenQuality==1:
                        agents[i].velocityLimitLow=topIndividuals[chosenInd].velocityLimitLow
                    elif chosenQuality==2:
                        agents[i].velocityLimitUp=topIndividuals[chosenInd].velocityLimitUp
                    elif chosenQuality==3:
                        agents[i].xDistUp=topIndividuals[chosenInd].xDistUp
                    else:
                        agents[i].yDistUp=topIndividuals[chosenInd].yDistUp



            #Mutate
            agents[i].mutate()


                #else:
                #   pygame.quit()
                #  sys.exit()
    

    #Texts
    score+=2
    scorestring = "Score: "+ str(score)
    textsurface = scorefont.render(scorestring,False,(200,130,200))
    screen.blit(textsurface,(20,20))

    #speedstring = "Velocity: "+ str(int(bird.velocity))
    #textsurface2 = scorefont.render(speedstring,False,(200,130,200))
    #screen.blit(textsurface2,(20,60))



    #draw info
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
    

    

    if harder:
        if score%20==0:
            pillarVelocity+=0.05
        
        if score%500==0:
            pillarFrequency+=1

    for a in range(len(agents)):
        agents[a].decide(birds[a],pillars)




    clock.tick(60)




