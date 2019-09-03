import sys
import os
import random
import time
import pygame
from pygame.locals import *
from pynput.keyboard import Key, Controller


#Seuraavaksi:
#Erittele filuihin
#Päätä: minkälaista AI? geneettinen, neuro with backprop, Q-learning, NEAT
#pelaamisesta oppiva


#Initialize controller

#keyboard = Controller()

#Initialize pygame
pygame.init()
pygame.font.init()



#Fonts and gavkground
scorefont = pygame.font.SysFont('Comic Sans MS',40)
gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
algofont = pygame.font.SysFont('Arial',20)
bg = pygame.image.load("clouds.png")




#Screen size
width,height=700,480
size = 1000,height



#Constants
ground=40
pillar=100
gap=100

pillarFrequency = 3
basePillarFrequency=pillarFrequency

pillargapL=-60
pillargapU= 100



#Colors
BLACK = 0,0,0
BLUE = 135,206,235
GREEN = 124,252,0
RED = 145,40,60
WHITE = 255,255,255


#Screen objects
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Demo")


#Bird Movement
x,y = 100,80
right = 1
left = 2
direction =0
size=[30,30]
velocity=0
acc=-0.6 
bump = 6


#Pillar movement
pillarVelocity=5
pillarpos=width

#Ticks and time and score
tickc=0
keytick=0
score=0
difficultyTick=0




#Object specifics

groundcolor=GREEN



#Pillar class

class Pillar:

    def __init__ (self,position):
        self.gap=100+(random.randint(pillargapL,pillargapU))
    def draw_pillar(self):
        self.upperPillar=pygame.Rect(self.pos,0,50,self.gap)
        self.lowerPillar=pygame.Rect(self.pos,self.gap+gap,50,height-ground-self.gap-gap)
        self.rectangles=[self.upperPillar,self.lowerPillar]
        pygame.draw.rect(screen,BLACK,pygame.Rect(self.pos,0,50,self.gap))
        pygame.draw.rect(screen,BLACK,pygame.Rect(self.pos,self.gap+gap,50,height-ground-self.gap-gap))
        

class Bird:



    def __init__(self):
        self.x=x
        self.y=y
        self.velocity=0
        self.rect=pygame.Rect(self.x,self.y,size[0],size[1])
        self.col=RED



    def bump(self):
        self.velocity +=bump


    def draw_bird(self):
        self.rect=pygame.Rect(self.x,self.y,size[0],size[1])
        pygame.draw.rect(screen,BLACK,pygame.Rect(self.x-2,self.y-2,size[0]+4,size[1]+4))
        pygame.draw.rect(screen,self.col,pygame.Rect(self.x,self.y,size[0],size[1]))


    def onGround(self):
        if (self.y>height-ground-40): 
            return True
        else:
            return False







#birds=[bird1,bird2,bird3,bird4,bird5]


start_time = None
clock = pygame.time.Clock ()


class Pillar:

    def __init__ (self,position):
        self.gap=100+(random.randint(pillargapL,pillargapU))
        self.pos=position
        self.velocity=pillarVelocity
        self.upperPillar=pygame.Rect(self.pos,0,50,self.gap)
        self.lowerPillar=pygame.Rect(self.pos,self.gap+gap,50,height-ground-self.gap-gap)
        self.rectangles=[self.upperPillar,self.lowerPillar]

    def move_pillar(self):
        self.pos=self.pos-pillarVelocity


    def draw_pillar(self):
        self.upperPillar=pygame.Rect(self.pos,0,50,self.gap)
        self.lowerPillar=pygame.Rect(self.pos,self.gap+gap,50,height-ground-self.gap-gap)
        self.rectangles=[self.upperPillar,self.lowerPillar]
        pygame.draw.rect(screen,BLACK,pygame.Rect(self.pos,0,50,self.gap))
        pygame.draw.rect(screen,BLACK,pygame.Rect(self.pos,self.gap+gap,50,height-ground-self.gap-gap))
        


#Mitä arvotaan: 
#kuinka kauan ennen painetaan up, x-suunta
#kuinka monta kertaa painataan up, y-suunta
#mikä on rajanopeus

pillars =[]
p=Pillar(width-50)
pillars.append(p) 
class Chromosome:


    def __init__(self):
        self.xDistUp=300
        self.yDistUp=50
        self.velocityLimitLow=-5
        self.velocityLimitUp=6
        self.endScore=0
        self.dead=False


    def randoms(self):
        self.xDistUp+=random.randint(-100,100)
        self.yDistUp+=random.randint(-50,50)
        self.velocityLimitLow+=(random.randint(-4,4)/4.0)
        self.velocityLimitUp+=(random.randint(-4,4)/4.0)


    def setEndScore(self,score):
        self.endScore=score

    def mutate(self):
        howMany=random.randint(1,4)
        
        if howMany==1:
            self.xDistUp+=random.randint(-40,40)
        elif howMany==2:
            self.yDistUp+=random.randint(-20,20)
        elif howMany==3: 
            self.velocityLimitLow+=(random.randint(-2,2)/4.0)
        else:
            self.velocityLimitUp+=(random.randint(-2,2)/4.0)     

    def decide(self,bird):
        nextPillar = next(x for x in pillars if x.pos-bird.x+20 > 0)
        gapUpperEdge = nextPillar.gap
        gapLowerEdge = nextPillar.gap+gap

    
        if (bird.y>gapUpperEdge+self.yDistUp and bird.x+self.xDistUp>nextPillar.pos and velocity<self.velocityLimitUp ):
            self.takeAction(bird)



        if (bird.velocity<self.velocityLimitLow):
            amount = int(round(abs((velocity/bump))))+1
            for x in range(amount):
                self.takeAction(bird)



    def takeAction(self,bird):
        bird.bump()
birds=[]
for a in range(40):
    birds.append(Bird())
    birds[a].col=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

agents=[]

for a in range(40):
    agents.append(Chromosome())
    agents[a].randoms()
#agents=[agent1,agent2,agent3,agent4,agent5]


topfitness=0
harder=False


#def qLearning():
    #https://pdfs.semanticscholar.org/c8d8/45063aedd44e8dbf668774532aa0c01baa4f.pdf





avgfitness=0






generation = []
gensize=10
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


        if(bird.velocity<-10):
            bird.velocity=-10
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
    for a in range(len(agents)):
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
    for i in range(len(birds)):
        for pillar in pillars:
            if ( agents[i].dead==False and birds[i].rect.colliderect(pillar.upperPillar) or birds[i].rect.colliderect(pillar.lowerPillar)):
                agents[i].setEndScore(score)
                agents[i].dead=True
                generation.append(agents[i])
                
    deadcount=0
    for i in range(len(agents)):
        if agents[i].dead:
            deadcount+=1


    topIndividuals=[]
    for i in range(10):
        topIndividuals.append(Chromosome)

   

    if deadcount==len(agents):
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

        for item in best:
            avgfitness+=item.endScore
        avgfitness=avgfitness/(1.0*len(best))
        if topfitness<best[0].endScore:
             topfitness=best[0].endScore
    
        for i in range(4):
            topIndividuals[i]=best[i]


        #Choose the 4 qualities from the five top individuals
        for i in range(len(agents)):
            agents[i]=Chromosome()
            qualities=[0,1,2,3]
            while len(qualities)!=0:        
                chosenInd=random.randint(0,3)
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
    datasurface=algofont.render("xD: "+distx,False,(0,0,0))
    screen.blit(datasurface,(750,50))
    datasurface=algofont.render("yD: "+disty,False,(0,0,0))
    screen.blit(datasurface,(750,75))
    datasurface=algofont.render("vL: "+vell,False,(0,0,0))
    screen.blit(datasurface,(750,100))
    datasurface=algofont.render("vU: "+velu,False,(0,0,0))
    screen.blit(datasurface,(750,125))




    pygame.display.flip()
    

    

    if harder:
        if score%20==0:
            pillarVelocity+=0.05
        
        if score%500==0:
            pillarFrequency+=1

    for a in range(len(agents)):
        agents[a].decide(birds[a])




    clock.tick(60)




