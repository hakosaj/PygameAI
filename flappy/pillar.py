import random
import pygame
from constants import *

class Pillar:
    #Pillar on siis korkeussuunnassa 0->gap ja self.gap+gap->height-ground-self.gap-gap
    #Pilarin alareuna siis matalimmillaan. 300
    #Pilarin alareuna siis korkeimmillaan 140
    #Linnun yläosa matalimmillaan 420
    #Linnun yläosa korkeimmillaan 0
    #
    def __init__ (self,position):
        self.gap=100+(random.randint(pillargapL,pillargapU))
        self.gap=150
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
        