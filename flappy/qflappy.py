import sys
import os
import random
import time
import pygame
import numpy as np
import math
from constants import *
from QAgent import QAgent
from bird import Bird
from selection import *
from pillar import Pillar
from pygame.locals import *
from pynput.keyboard import Key, Controller

    """Main executable for the flappy q-learning.
    """

# Initialize pygame
pygame.init()
pygame.font.init()
# Fonts and gavkground
scorefont = pygame.font.SysFont("Comic Sans MS", 40)
gameoverfont = pygame.font.SysFont("Comic Sans MS", 40)
algofont = pygame.font.SysFont("Arial", 20)
bg = pygame.image.load("clouds.png")


start_time = None
clock = pygame.time.Clock()
startGap = 250

# Mitä arvotaan:
# kuinka kauan ennen painetaan up, x-suunta
# kuinka monta kertaa painataan up, y-suunta
# mikä on rajanopeus
pillars = []
p = Pillar(width - startGap)
pillars.append(p)
harder = True
iterations = 0


# Algos:0 is normal game, 1 is GA
print("Chosen algorithm: Q-learning")
chosenAlgo = 2
dead = False
discount = 1
qAgent = QAgent(discount)
if len(sys.argv) == 3:
    qAgent.loadMatrix(sys.argv[2])
actionTaken = False
previousAction = 0
birds = []


agentsc = 1
birds.append(Bird())


while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.event.clear()
                event = pygame.event.wait()
                while event.key != pygame.K_p:
                    pygame.event.clear()
                    event = pygame.event.wait()

            if event.key == pygame.K_SPACE:
                birds[0].bump()

            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Bird movement
    for bird in birds:
        bird.velocity += acc

        bird.y = bird.y - bird.velocity
        if bird.velocity > 10:
            bird.velocity = 10

        if bird.y > height - ground - 40:
            bird.y = height - ground - size[1]

        if bird.y < 0:
            bird.y = 0

    # draw static
    screen.fill(WHITE)
    screen.blit(bg, (0, 0))
    pygame.draw.rect(
        screen, groundcolor, pygame.Rect(0, height - ground, width, ground)
    )
    pygame.draw.rect(screen, BLACK, pygame.Rect(width, 0, 5, height))

    # birb
    birds[0].draw_bird()

    # pillar

    tickc += 1
    if tickc == int(round(width / (5 * pillarFrequency))):
        pillars.append(Pillar(width - 50))
        tickc = 0

    for pillar in pillars:
        pillar.move_pillar()
        pillar.draw_pillar()
        if pillar.pos < -600:
            pillars.remove(pillar)

    collide = False
    for pillar in pillars:
        if birds[0].rect.colliderect(pillar.upperPillar) or birds[0].rect.colliderect(
            pillar.lowerPillar
        ):
            collide = True

    if collide:
        birds[0].dead = True
        score = 0
        tickc = 0
        keytick = 0
        bird.velocity = 0
        score = 0
        difficultyTick = 0
        pillarVelocity = 5
        pillarFrequency = basePillarFrequency
        birds[0].y = y + (random.randint(-100, 200))
        # birds[0].y=y
        pillars.clear()
        p = Pillar(width - startGap)
        pillars.append(p)

    else:
        birds[0].dead = False

    score += 2
    scorestring = "Score: " + str(score)
    textsurface = scorefont.render(scorestring, False, (200, 130, 200))
    screen.blit(textsurface, (20, 20))

    try:
        nextPillar = next(x for x in pillars if x.pos > bird.x)
        speedstring = "Xdist: " + str(int(nextPillar.pos - birds[0].x))
        speedstring2 = "Ydist:" + str(int(nextPillar.gap + gap / 2 - birds[0].y))
        textsurface2 = scorefont.render(speedstring, False, (200, 130, 200))
        textsurface3 = scorefont.render(speedstring2, False, (200, 130, 200))
        screen.blit(textsurface2, (20, 60))
        screen.blit(textsurface3, (20, 90))
    except StopIteration:
        pass

    pygame.display.flip()

    harder = False
    if harder:
        if score % 100 == 0:
            pillarVelocity += 0.05

        if score % 2000 == 0:
            pillarFrequency += 1

    # Q-learning
    if True:
        xdistToPillar = int(nextPillar.pos - birds[0].x)
        ydistToPillar = int(nextPillar.gap * 1.5 - birds[0].y)

        if actionTaken:
            # 3) observe outcome state and reward
            outcomeState = [ydistToPillar, xdistToPillar]
            if birds[0].dead:
                reward = -1000
            else:
                reward = 0

            # 4) update matrix based on bellmann equation
            # new state in matrix = old state value + learningRate*
            # https://www.semanticscholar.org/paper/Applying-Q-Learning-to-Flappy-Bird-Ebeling-Rump-Hervieux-Moore/c8d845063aedd44e8dbf668774532aa0c01baa4f
            # new state r = discount*max value state+1
            # jommallakummalla actionilla - Q edellisessä
            previousStateValue = qAgent.getFromQ(previousAction, stateHold)
            if previousAction == 0:
                otherAction = 1
            else:
                otherAction = 0

            # alpha = 1/qAgent.updateStateCount(stateHold)
            # print(alpha)

            newMaxStateValue = qAgent.discount * max(
                qAgent.getFromQ(previousAction, outcomeState),
                qAgent.getFromQ(otherAction, outcomeState),
            )
            addToMatrix = previousStateValue + 0.7 * (
                reward + newMaxStateValue - previousStateValue
            )
            qAgent.updateQMatrix(previousAction, stateHold, addToMatrix)
            iterations += 1

            if iterations % 30000 == 0:
                np.save(
                    "flappyQData//flappyNotRandomIteration" + str(iterations),
                    qAgent.QMatrix,
                )
            # print("add: ",reward+newMaxStateValue)

        # 1)determine action
        stateHold = [ydistToPillar, xdistToPillar]
        actionNot = qAgent.getFromQ(0, stateHold)
        actionBump = qAgent.getFromQ(1, stateHold)
        print("Action: not ", actionNot, " ,bump ", actionBump)
        # 2)take action
        if actionBump > actionNot:

            previousAction = 1
            birds[0].bump()
        else:
            previousAction = 0

        actionTaken = True

    clock.tick(120)
