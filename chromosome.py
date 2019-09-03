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
        self.xDistUp+=random.randint(-150,150)
        self.yDistUp+=random.randint(-70,70)
        self.velocityLimitLow+=(random.randint(-5,5)/4.0)
        self.velocityLimitUp+=(random.randint(-5,5)/4.0)


    def setEndScore(self,score):
        self.endScore=score

    def mutate(self):
        howMany=random.randint(1,4)
        
        if howMany==1:
            self.xDistUp+=mutationRate*random.randint(-30,30)
        elif howMany==2:
            self.yDistUp+=mutationRate*random.randint(-20,20)
        elif howMany==3: 
            self.velocityLimitLow+=mutationRate*(random.randint(-1,1)/4.0)
        else:
            self.velocityLimitUp+=mutationRate*(random.randint(-2,2)/4.0)     

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