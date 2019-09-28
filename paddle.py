
import pygame
from breakconstants import *


class Paddle:



    def __init__(self):
        self.x=x
        self.y=y
        self.points=10
        self.rect=pygame.Rect(self.x+4,self.y+4,blockX-8,blockY-8)
        self.col=(random.randint(0,255),random.randint(0,255),random.randint(0,255))


    def draw_block(self):
        pygame.draw.rect(screen,BLACK,pygame.Rect(self.x,self.y,blockX,blockY))
        pygame.draw.rect(screen,self.col,self.rect)

        