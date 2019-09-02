import sys
import random
import pygame
from pynput.keyboard import Key, Controller

#Seuraavaksi:
#Erittele filuihin
#Päätä: minkälaista AI? geneettinen, neuro with backprop, Q-learning, NEAT
#pelaamisesta oppiva


#Initialize controller

keyboard = Controller()

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
        

class Bird:



    def __init__(self):
        self.x=x
        self.y=y
        self.velocity=0
        self.rect=pygame.Rect(self.x,self.y,size[0],size[1])



    def bump(self):
        self.velocity +=bump


    def draw_bird(self):
        self.rect=pygame.Rect(self.x,self.y,size[0],size[1])
        pygame.draw.rect(screen,RED,pygame.Rect(self.x,self.y,size[0],size[1]))


    def onGround(self):
        if (self.y>height-ground-40): 
            return True
        else:
            return False





pillars =[]
p=Pillar(width-50)
pillars.append(p) 

bird1 = Bird()
bird2 = Bird()
bird2.x+=50
birds=[bird1,bird2]




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

class Chromosome:


    def __init__(self):
        self.xDistUp=300
        self.yDistUp=50
        self.velocityLimitLow=-5
        self.velocityLimitUp=6
        self.endScore=0


    def randoms(self):
        self.xDistUp+=random.randint(-50,50)
        self.yDistUp+=random.randint(-20,20)
        self.velocityLimitLow+=(random.randint(-2,2)/2.0)
        self.velocityLimitUp+=(random.randint(-2,2)/2.0)


    def setEndScore(self,score):
        self.endScore=score


    def mutate(self):
        self.xDistUp+=random.randint(-20,20)
        self.yDistUp+=random.randint(-20,20)
        self.velocityLimitLow+=random.randint(-1,1)
        self.velocityLimitUp+=random.randint(-1,1)       

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


agent1 = Chromosome()
agent2 = Chromosome()
agents=[agent1,agent2]


harder=False


#def qLearning():
    #https://pdfs.semanticscholar.org/c8d8/45063aedd44e8dbf668774532aa0c01baa4f.pdf

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


    #draw dynamic

    #birb
    for bird in birds:
        bird.draw_bird()
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
    for pillar in pillars:
        for i in range(len(birds)):
            if (birds[i].rect.colliderect(pillar.upperPillar) or birds[i].rect.colliderect(pillar.lowerPillar)):

                #endstring = "YOU LOSE. FINAL SCORE: "+ str(score)
                #retrystring= "PRESS R TO RETRY, ANY BUTTON TO QUIT"


                #endsurface = gameoverfont.render(endstring,False,(255,255,200))
                #screen.blit(endsurface,(150,150))
                #retrysurface = gameoverfont.render(retrystring,False,(255,255,200))
                #screen.blit(retrysurface,(80,200))
                #pygame.display.flip()

                #pygame.event.clear()
                #event = pygame.event.wait()
                #while (event.type!=pygame.KEYDOWN):
                    #event=pygame.event.wait()
                #if (event.key==pygame.K_r):
                agents[i].setEndScore(score)
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
                generation.append(agents[i])
                agents[i]=Chromosome()
                agents[i].randoms() 

                #else:
                #   pygame.quit()
                #  sys.exit()
    

    #Texts
    score+=2
    scorestring = "Score: "+ str(score)
    textsurface = scorefont.render(scorestring,False,(200,130,200))
    screen.blit(textsurface,(20,20))



    speedstring = "Velocity: "+ str(int(bird.velocity))
    textsurface2 = scorefont.render(speedstring,False,(200,130,200))
    screen.blit(textsurface2,(20,60))



    #draw info
    distx=str(agent1.xDistUp)
    disty=str(agent1.yDistUp)
    vell=str(agent1.velocityLimitLow)
    velu=str(agent1.velocityLimitUp)
    individual=str(len(generation)+1)

    datasurface=algofont.render("DistX: "+distx,False,(0,0,0))
    screen.blit(datasurface,(730,30*(1)))
    datasurface=algofont.render("DistY: "+disty,False,(0,0,0))
    screen.blit(datasurface,(730,30*(2)))
    datasurface=algofont.render("VelocityLimitUp: "+vell,False,(0,0,0))
    screen.blit(datasurface,(730,30*(3)))
    datasurface=algofont.render("VelocityLimitLow: "+velu,False,(0,0,0))
    screen.blit(datasurface,(730,30*(4)))
    datasurface=algofont.render("Individual: "+individual+"/"+str(gensize),False,(0,0,0))
    screen.blit(datasurface,(730,5*(1)))

    pygame.display.flip()
    

    for i in range(len(generation)):
        datasurface=algofont.render(str(i+1)+": "+str(generation[i].endScore),False,(0,0,0))
        screen.blit(datasurface,(730,140+30*(i)))
    
    pygame.display.flip()

    if harder:
        if score%20==0:
            pillarVelocity+=0.05
        
        if score%500==0:
            pillarFrequency+=1


    agent1.decide(bird1)
    agent2.decide(bird2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

    clock.tick(30)




