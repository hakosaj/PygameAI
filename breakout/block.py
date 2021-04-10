import pygame
from breakconstants import *

"""Block class for the breakout game
"""


class Block:
    def __init__(self, x, y):
        """Initialize block

        Args:
            x (int): left x coordinate of the block
            y (int): upper y coordinate of the block
        """
        self.x = x
        self.y = y
        self.points = 10
        self.rect = pygame.Rect(self.x + 4, self.y + 4, blockX - 8, blockY - 8)
        self.col = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    def centerX(self):
        """Get center x of the block

        Returns:
            float: center x coord
        """
        return self.x + 0.5 * blockX

    def centerY(self):
        """Get center y of the block

        Returns:
            float: center y coord
        """
        return self.y + 0.5 * blockY

    def draw_block(self):
        """Draw the block"""
        pygame.draw.rect(screen, BLACK, pygame.Rect(self.x, self.y, blockX, blockY))
        pygame.draw.rect(screen, self.col, self.rect)
