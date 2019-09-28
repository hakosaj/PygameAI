import pygame
import math
from breakconstants import *


class Ball:



    def __init__(self,ballRadius):
        self.x=200
        self.y=300
        self.xv=0
        self.yv=-ballVelocity
        self.radius=ballRadius
        self.circ=pygame.Rect(self.x,self.y,self.radius,self.radius)

    def centerX(self):
        return self.x+0.5*self.radius

    def centerY(self):
        return self.y+0.5*self.radius


    def move_ball(self):
        #if (self.y-self.radius>0 and self.y+self.radius+<height-60):
        if (self.y-self.radius>0):
            self.y+=self.yv
        else:
            self.yv=-self.yv
            self.y+=self.yv

        if (self.x-self.radius>0 and self.x+self.radius<width):
            self.x+=self.xv
        else:
            self.xv=-self.xv
            self.x+=self.xv

    def draw_ball(self):
        self.circ=pygame.Rect(self.x,self.y,self.radius,self.radius)
        pygame.draw.circle(screen,BLACK,(round(self.x),round(self.y)),self.radius+2)
        pygame.draw.circle(screen,WHITE,(round(self.x),round(self.y)),self.radius)

        