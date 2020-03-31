import pygame
from constants import *

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

