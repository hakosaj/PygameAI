import sys
import os
import random
import time
import pygame
import math
from pygame.locals import *
from pynput.keyboard import Key, Controller
from breakconstants import *
from block import Block
from paddle import Paddle
from ball import Ball



def sign(a):
    if a>0:
        return 1
    else:
        return -1

#Initialize pygame
pygame.init()
pygame.font.init()
#Fonts and gavkground
scorefont = pygame.font.SysFont('Comic Sans MS',40)
gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
algofont = pygame.font.SysFont('Arial',20)

paddle=Paddle(paddlewidth)
ball=Ball(ballRadius)
blocks=[]

#for row in range(0,blocksY+2):
 #   for col in range(0,blocksX-6):
  #      blocks.append(Block(leftMargin+(col+5)*blockX,upMargin+row*blockY+100)) 


for row in range(0,blocksY):
    for col in range(0,blocksX):
        blocks.append(Block(leftMargin+col*blockX,upMargin+row*blockY)) 




start_time = None
clock = pygame.time.Clock ()

justCollided=False

tickcounter=0



def automaticMove(paddle,ball):
    if paddle.x+(paddle.width/2)<ball.centerX()-rightMargin:
        paddle.move_paddle(2*paddleSpeed)
    if paddle.x+(paddle.width/2)>ball.centerX()+rightMargin:
        paddle.move_paddle(2*-paddleSpeed)


while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                pygame.event.clear()
                event = pygame.event.wait()
                while (event.key!=pygame.K_o):
                    pygame.event.clear()
                    event = pygame.event.wait()                    

            if event.key == pygame.K_RIGHT:
               paddle.move_paddle(paddleSpeed) 
            if event.key == pygame.K_LEFT:
               paddle.move_paddle(-paddleSpeed)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()  
    if keys[pygame.K_RIGHT]:
        paddle.move_paddle(paddleSpeed) 
    if keys[pygame.K_LEFT]:
        paddle.move_paddle(-paddleSpeed)

    justCollided=False

    #Collision to paddle 
    if paddle.rect.colliderect(ball.circ) and not justCollided:
        ball.yv=-ball.yv
        ball.xv= paddleVelocityModifier*(((ball.x-paddle.x)/paddle.width*1.00)-0.5)

        modifier=0
        while abs(modifier)<4:
            modifier=random.randint(-10,10)
        ball.xv=ball.xv+(paddleBounceModifier*1.0/modifier)

        justCollided=True
        tickcounter=0


    #Collision to blocks
    for block in blocks:
        if ball.circ.colliderect(block.rect):
            justCollided=True


            verticalCenterDifference = ball.centerY()+ballRadius-block.centerY()
            horizontalCenterDifference = ball.centerX()+ballRadius-block.centerX()


            if abs(verticalCenterDifference)<blockY*0.45:
                ball.xv=-ball.xv

            if abs(horizontalCenterDifference)<blockX*0.45:
                ball.yv=-ball.yv

            modifier=0
            while abs(modifier)<4:
                modifier=random.randint(-10,10)
            ball.xv=ball.xv+(blockBounceModifier*1.0/modifier)
            blocks.remove(block)

            #Difficulty scaling

            if len(blocks)%blocksY==0:
                ball.yv= ball.yv*1.2 
            

    if (justCollided and tickcounter==1):
        tickcounter=0
        justCollided=False



    

    else:
        ball.move_ball()

    screen.fill(BROWN)
    for block in blocks:
        block.draw_block()
    paddle.draw_paddle()
    ball.draw_ball()



    #reset
    if ball.centerY()>width:
        blocks=[]

        for row in range(0,blocksY):
            for col in range(0,blocksX):
                blocks.append(Block(leftMargin+col*blockX,upMargin+row*blockY))
        ball.xv=0
        ball.yv=10
        ball.x=200
        ball.y=300




        #draw info
        #screen.blit(datasurface,(750,10))
        #datasurface=algofont.render("Avg fit: "+str(avgfitness),False,(0,0,0))
        #screen.blit(datasurface,(750,30))
        #datasurface=algofont.render("Generation: "+str(currentGeneration),False,(0,0,0))
        #screen.blit(datasurface,(750,50))
        #datasurface=algofont.render("Alive: "+str(agentsc-deadcount)+"/"+str(agentsc),False,(0,0,0))
        #screen.blit(datasurface,(750,70))






    automaticMove(paddle,ball)
    tickcounter+=1
    pygame.display.flip()
    clock.tick(30)




