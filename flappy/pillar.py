import random
import pygame
from constants import *


class Pillar:
    """Pillar class for the flappy game. Y-direction is so that pillar starts from 0 and extends until gap, gap is between self.gap+gap, lower ifrom that to height-ground-self.gap-gap
    """
    # Pillar on siis korkeussuunnassa 0->gap ja self.gap+gap->height-ground-self.gap-gap
    # Pilarin alareuna siis matalimmillaan. 300
    # Pilarin alareuna siis korkeimmillaan 140
    # Linnun yläosa matalimmillaan 420
    # Linnun yläosa korkeimmillaan 0
    #
    def __init__(self, position. random=True):
        """Initialize a pillar. 

        Args:
            position (int): x-position of the pillar
            random (bool): Random gap or predetermined
        """
        if random:
            self.gap = 100 + (random.randint(pillargapL, pillargapU))
        else:
            self.gap=150
        self.pos = position
        self.velocity = pillarVelocity
        self.upperPillar = pygame.Rect(self.pos, 0, 50, self.gap)
        self.lowerPillar = pygame.Rect(
            self.pos, self.gap + gap, 50, height - ground - self.gap - gap
        )
        self.rectangles = [self.upperPillar, self.lowerPillar]

    def move_pillar(self):
        """Move pillar to a direction of the velocity
        """
        self.pos = self.pos - pillarVelocity

    def draw_pillar(self):
        """Draw a pillar
        """
        self.upperPillar = pygame.Rect(self.pos, 0, 50, self.gap)
        self.lowerPillar = pygame.Rect(
            self.pos, self.gap + gap, 50, height - ground - self.gap - gap
        )
        self.rectangles = [self.upperPillar, self.lowerPillar]
        pygame.draw.rect(screen, BLACK, pygame.Rect(self.pos, 0, 50, self.gap))
        pygame.draw.rect(
            screen,
            BLACK,
            pygame.Rect(self.pos, self.gap + gap, 50, height - ground - self.gap - gap),
        )
