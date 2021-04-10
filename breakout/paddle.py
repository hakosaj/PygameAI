import pygame
import math
from breakconstants import *


    """Paddle class for the breakout game

    """

class Paddle:
    def __init__(self, width):
        """Initialize game paddle

        Args:
            width (float): paddle width
        """
        self.x = 200
        self.y = height - 60
        self.width = width
        self.rect = pygame.Rect(self.x + 5, self.y + 5, self.width - 10, 40 - 10)

    def move_paddle(self, offset):
        """Move paddle according to the offset parameter

        Args:
            offset ([type]): [description]
        """
        if self.x + offset > 0 and self.x + offset + self.width < width:
            self.x += offset

    def center(self):
        """get paddle centerpoint

        Returns:
            float: paddle centerpoint
        """
        return self.x + 0.5 * self.width

    def draw_paddle(self):
        """Draw the paddle component
        """
        self.rect = pygame.Rect(self.x, self.y, self.width, 40)
        pygame.draw.rect(screen, BLACK, pygame.Rect(self.x, self.y, self.width, 40))
        pygame.draw.rect(screen, WHITE, self.rect)
