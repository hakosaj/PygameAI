import sys
import os
import random
import time
import pygame
import math
from block import Block
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller
from grid import *


def moveBlock(b,g, xdif,ydif):
    bx=b.x+xdif
    by=b.y+ydif
    copy=b
    if (b.leftEdge()+xdif<0 or b.rightEdge()+xdif==gridsizex or b.bottomEdge()==gridsizey-1):
        return b
    ofs=b.offset
    g.removeBlock(b)
    b = Block(bx,by,"j",g)
    b.createConfiguration(ofs)
    for block in g.blocks:
        if (block.collidesWith(b)):
            copy.stop()
            return copy
    g.addBlock(b)
    return b




#Tetris grid
gridsizex=15
gridsizey=30
g = Grid(gridsizex,gridsizey)

#Screen objects
g.createSquares()
b = Block(5,5,"j",g)
b.createConfiguration(0)
g.addBlock(b)




#Initialize pygame
pygame.init()
pygame.font.init()
#Fonts and gavkground
scorefont = pygame.font.SysFont('Comic Sans MS',40)
gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
algofont = pygame.font.SysFont('Arial',20)







start_time = None
clock = pygame.time.Clock ()


tickcounter=0


activeBlock=b

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                pygame.event.clear()
                event = pygame.event.wait()
                while (event.key!=pygame.K_o):
                    pygame.event.clear()
                    event = pygame.event.wait()                    
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                g.modifyBlock(activeBlock)
            elif event.key == pygame.K_RIGHT:
                activeBlock=moveBlock(activeBlock,g,1,0)
            elif event.key == pygame.K_DOWN:
                activeBlock=moveBlock(activeBlock,g,0,1)
            elif event.key == pygame.K_LEFT:
                activeBlock=moveBlock(activeBlock,g,-1,0)
            elif event.key == pygame.K_r:
                g.printGrid()


    g.drawGrid()

    if (tickcounter%20==0):
        activeBlock=moveBlock(activeBlock,g,0,1)

            


    if (activeBlock.bottomEdge()==gridsizey-1 or activeBlock.isStopped):
        activeBlock.stop()
        activeBlock = Block(5,5,"j",g)
        activeBlock.createConfiguration(0)
        g.addBlock(activeBlock)



    tickcounter+=1
    pygame.display.flip()
    clock.tick(20)




