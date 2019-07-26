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
bg = pygame.image.load("clouds.png")




#Screen size
width,height=700,480
size = 1000,height



#Constants
ground=40
pillar=100
gap=100

pillarFrequency = 2
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
bump = 5


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

bird = Bird()




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
        



class BaseAgent:

    #Knowledge: distance to next pillar, own velocity, gap distances

    def __init__(self,learningRate):
        self.rate=learningRate
        self.nextPillar=0
        self.yVelocity=0
        self,gapUpper=0
        self.gapLower


    def update_status(self)

    def takeAction():
        keyboard.press(Key.space)
        keyboard.release(Key.space)


    def retry():
        keyboard.press('r')
        keyboard.release('r')

agent = BaseAgent(0.1)




def baseai():

    y_ai = bird.y
    x_ai = bird.x
    velocity=bird.velocity
    pillarDists=[]

    nextPillar = next(x for x in pillars if x.pos-x_ai+40 > 0)


    gapUpperEdge = nextPillar.gap
    gapLowerEdge = nextPillar.gap+gap
    

    if (velocity<-5):
        amount = int(round(abs((velocity/bump))))+1
        for x in range(amount):
            keyboard.press(Key.space)
            keyboard.release(Key.space)



    if (y_ai>gapUpperEdge+(gap/2)):
        keyboard.press(Key.space)
        keyboard.release(Key.space)

    #if (y_ai>gapUpperEdge+gap*3):
     #   keyboard.press(Key.space)
      #  keyboard.release(Key.space)






    










while True:



    
    
    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.bump()

            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    #Bird movement
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
        if (bird.rect.colliderect(pillar.upperPillar) or bird.rect.colliderect(pillar.lowerPillar)):

            endstring = "YOU LOSE. FINAL SCORE: "+ str(score)
            retrystring= "PRESS R TO RETRY, ANY BUTTON TO QUIT"


            endsurface = gameoverfont.render(endstring,False,(255,255,200))
            screen.blit(endsurface,(150,150))
            retrysurface = gameoverfont.render(retrystring,False,(255,255,200))
            screen.blit(retrysurface,(80,200))
            pygame.display.flip()

            pygame.event.clear()
            event = pygame.event.wait()
            while (event.type!=pygame.KEYDOWN):
                event=pygame.event.wait()
            if (event.key==pygame.K_r):
                score=0
                tickc=0
                keytick=0
                score=0
                difficultyTick=0
                pillarVelocity=5
                pillarFrequency=basePillarFrequency
                bird.y=y
                pillars.clear()
                p=Pillar(width-50)
                pillars.append(p) 

            else:
                pygame.quit()
                sys.exit()
    

    #Texts
    score+=2
    scorestring = "Score: "+ str(score)
    textsurface = scorefont.render(scorestring,False,(200,130,200))
    screen.blit(textsurface,(20,20))



    speedstring = "Velocity: "+ str(int(bird.velocity))
    textsurface2 = scorefont.render(speedstring,False,(200,130,200))
    screen.blit(textsurface2,(20,60))





        
    
    pygame.display.flip()


    if score%20==0:
        pillarVelocity+=0.05
    
    if score%500==0:
        pillarFrequency+=1

    baseai()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

    clock.tick(30)




