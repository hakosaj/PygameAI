import pygame
from constants import *

"""Flappy bird class for the bird object
"""


class Bird:
    def __init__(self):
        """Initialize the bird"""
        self.x = x
        self.y = y
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.col = LIGHTGRAY
        self.cnn = True

    def bump(self):
        """Take action"""
        self.velocity += bump

    def draw_bird(self):
        """Draw the bird"""
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        if not self.cnn:
            pygame.draw.rect(
                screen,
                BLACK,
                pygame.Rect(self.x - 2, self.y - 2, size[0] + 4, size[1] + 4),
            )
        pygame.draw.rect(
            screen, self.col, pygame.Rect(self.x, self.y, size[0], size[1])
        )

    def onGround(self):
        """Is the bird on ground

        Returns:
            bool: is the bird on the ground
        """
        if self.y > height - ground - 40:
            return True
        else:
            return False
