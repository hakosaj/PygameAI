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


currentOne="l"
#configurations = i j t o s z l
currentOnes=["i","j","t","o","s","l"]

def moveBlock(b,g, xdif,ydif):
    bx=b.x+xdif
    by=b.y+ydif
    copy=b
    if (b.leftEdge()+xdif<0 or b.rightEdge()+xdif==gridsizex or b.bottomEdge()==gridsizey-1):
        return b
    ofs=b.offset
    g.removeBlock(b)
    b = Block(bx,by,currentOne,g)
    b.createConfiguration(ofs)

    #If does bottom collide, needs to stop in any case. If not, return the moved block unless
    #side collisiojn has occurred.

    #Copy here is the nonmoved block, so bottom collision: if direction is down (=ydif==1) and bottomedge is 1 above other block
    for block in g.blocks:
        if (ydif==1 and block.collidesWithBottom(copy)):
            print("bot collided")
            copy.stop()
            return copy
        if (block.collidesWith(b)):
            print("side collided")
            return copy
    g.addBlock(b)
    return b




#Tetris grid
gridsizex=15
gridsizey=30
g = Grid(gridsizex,gridsizey)

#Screen objects
g.createSquares()
b = Block(5,5,currentOne,g)
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
                if (activeBlock.configuration=="l"):
                    if not ((activeBlock.offset==2 and activeBlock.x>12) or (activeBlock.offset==6 and activeBlock.x>13) ):
                        g.modifyBlock(activeBlock)
                else:
                    if (activeBlock.configuration!="o"):
                        g.modifyBlock(activeBlock)

            
            elif event.key == pygame.K_RIGHT:
                activeBlock=moveBlock(activeBlock,g,1,0)
            elif event.key == pygame.K_DOWN:
                activeBlock=moveBlock(activeBlock,g,0,1)
            elif event.key == pygame.K_LEFT:
                activeBlock=moveBlock(activeBlock,g,-1,0)
            elif event.key == pygame.K_LSHIFT:
                for i in range(gridsizey):
                    activeBlock=moveBlock(activeBlock,g,0,1)

            elif event.key == pygame.K_r:
                g.printGrid()


    g.drawGrid()

    if (tickcounter%20==0):
        activeBlock=moveBlock(activeBlock,g,0,1)




            


    if ( (activeBlock.bottomEdge()==gridsizey-1 or activeBlock.isStopped)):
        activeBlock.stop()
        g.addBlock(activeBlock)
        currentOne=random.choice(currentOnes)
        activeBlock = Block(5,5,currentOne,g)
        activeBlock.createConfiguration(0)
        g.addBlock(activeBlock)


    tickcounter+=1
    pygame.display.flip()
    clock.tick(20)




