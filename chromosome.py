import random
from pillar import Pillar
from bird import Bird
from flappyConstants import *

class Chromosome:


    def __init__(self):
        self.xDistUp=300
        self.yDistUp=50
        self.velocityLimitLow=-5
        self.velocityLimitUp=6
        self.endScore=0
        self.dead=False


    def randoms(self):
        self.xDistUp+=random.randint(-200,200)
        self.yDistUp+=random.randint(-120,120)
        self.velocityLimitLow+=(random.randint(-5,5)/2.0)
        self.velocityLimitUp+=(random.randint(-5,5)/2.0)


    def reset(self):
        self.xDistUp=300
        self.yDistUp=50
        self.velocityLimitLow=-5
        self.velocityLimitUp=6
        self.mutate(1)


    def setEndScore(self,score):
        self.endScore=score

    def mutate(self,mutationTrigger):
        howMany =random.randint(2,3)
        for i in range (howMany):
            which=random.randint(1,4)
            
            if which==1:
                self.xDistUp+=mutationTrigger*mutationRate*random.randint(-40,40)
            elif which==2:
                self.yDistUp+=mutationTrigger*mutationRate*random.randint(-20,20)
            elif which==3: 
                self.velocityLimitLow+=mutationTrigger*mutationRate*(random.randint(-2,2)/6.0)
            else:
                self.velocityLimitUp+=mutationTrigger*mutationRate*(random.randint(-2,2)/5.0)     

    def decide(self,bird,pillars):
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