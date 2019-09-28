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

for row in range(0,blocksY):
    for col in range(0,blocksX):
        blocks.append(Block(leftMargin+col*blockX,upMargin+row*blockY)) 



start_time = None
clock = pygame.time.Clock ()

justCollided=False

tickcounter=0



def automaticMove(paddle,ball):
    while paddle.x+paddle.width<ball.centerX()-rightMargin:
        paddle.move_paddle(paddleSpeed)
    while paddle.x>ball.centerX()+
    rightMargin:
        paddle.move_paddle(-paddleSpeed)


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

        justCollided=True
        tickcounter=0


    #Collision to blocks
    for block in blocks:
        if ball.circ.colliderect(block.rect):
            justCollided=True

            #Oikealla, jos y-suunnassa keskipisteiden ero on alle puol blockin korkeutta ja pallon kk on yli puol 
            #blockin pituutta oikealle blockin kestarista

            verticalCenterDifference = ball.centerY()-block.centerY()
            horizontalCenterDifference = ball.centerX()-block.centerX()

            #Jos itseisarvo on isompi kuin blockin puolikas dimensio, tämänsuuntainen törmäys tapahtuu
            if abs(verticalCenterDifference)<=blockY*0.5:
                ball.yv=-ball.yv

            elif abs(horizontalCenterDifference)<blockX*0.5:
                ball.xv=-ball.xv
            else:
                pass

            blocks.remove(block)
            

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




