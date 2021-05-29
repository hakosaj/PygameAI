import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller


class Square:
    """One tetris square"""

    def __init__(self, xcoord, ycoord):
        """Initialize the square

        Args:
            xcoord (int): x coordinate in the grid
            ycoord (int): y coordinate in the grid
        """

        self.xcoord = xcoord
        self.ycoord = ycoord
        self.x = xcoord * blocksize
        self.y = ycoord * blocksize
        self.status = 0
        self.color = WHITE

    # statuses: 0 empty, 1 landed, 2 moving

    def changeStatus(self, newStatus):
        """Change status of the block

        Args:
            newStatus (bool): new status
        """
        self.status = newStatus

    def changeColor(self, col):
        """Change block color

        Args:
            col (pygame.Color): new color
        """
        self.color = col

    def drawSquare(self, currentColor):
        """Draw this square and its edges

        Args:
            currentColor (pygame.Color): if status is other, then color with this
        """
        ro = pygame.Rect(self.x, self.y, blocksize, blocksize)
        ri = pygame.Rect(self.x + 1, self.y + 1, blocksize - 1, blocksize - 1)
        pygame.draw.rect(screen, BLACK, ro)
        if self.status == 0:
            pygame.draw.rect(screen, WHITE, ri)
        elif self.status == 1:
            pygame.draw.rect(screen, self.color, ri)
        else:
            pygame.draw.rect(screen, currentColor, ri)
