import random
import pygame
from flappyConstants import *

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
        