
import pygame
import math
from breakconstants import *


class Paddle:



    def __init__(self,width):
        self.x=200
        self.y=height-60
        self.width=width
        self.rect=pygame.Rect(self.x+5,self.y+5,self.width-10,40-10)


    def move_paddle(self,offset):
        if (self.x+offset>0 and self.x+offset+self.width<width):
            self.x+=offset


    def draw_paddle(self):
        self.rect=pygame.Rect(self.x,self.y,self.width,40)
        pygame.draw.rect(screen,BLACK,pygame.Rect(self.x,self.y,self.width,40))
        pygame.draw.rect(screen,WHITE,self.rect)

        