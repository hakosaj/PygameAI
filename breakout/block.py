import pygame
from breakconstants import *


class Block:



    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.points=10
        self.rect=pygame.Rect(self.x+4,self.y+4,blockX-8,blockY-8)
        self.col=(random.randint(0,255),random.randint(0,255),random.randint(0,255))


    def centerX(self):
            return self.x+0.5*blockX

    def centerY(self):
            return self.y+0.5*blockY


    def draw_block(self):
        pygame.draw.rect(screen,BLACK,pygame.Rect(self.x,self.y,blockX,blockY))
        pygame.draw.rect(screen,self.col,self.rect)

        