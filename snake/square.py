import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *


class Square:
    def __init__(self, xcoord, ycoord):
        """Initialize the square

        Args:
            xcoord (int): xcoord
            ycoord (int): ycoord
        """
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.x = xcoord*blocksize
        self.y = ycoord*blocksize
        self.food=False
        self.snake=False
        self.path=False
        self.index=-1

    def setFood(self, bol):
        """Set food to this square

        Args:
            bol (bool): food boolean
        """
        self.food = bol

    def drawSquare(self):
        """Draw a grid square
        """
        ro = pygame.Rect(self.x, self.y, blocksize, blocksize)
        ri = pygame.Rect(self.x + 1, self.y + 1, blocksize - 1, blocksize - 1)
        pygame.draw.rect(screen, BLACK, ro)
        if self.food:
            pygame.draw.rect(screen, GREEN, ri)
        elif self.snake:
            pygame.draw.rect(screen, RED, ri)
        elif self.path:
            pygame.draw.rect(screen, YELLOW, ri)
        else:
            pygame.draw.rect(screen, BLACK, ri)

    def drawSnakeSquare(self):
        """Draw a snake square
        """
        ro = pygame.Rect(self.x, self.y, blocksize, blocksize)
        ri = pygame.Rect(self.x + 1, self.y + 1, blocksize - 1, blocksize - 1)
        pygame.draw.rect(screen, BLACK, ro)
        pygame.draw.rect(screen, RED, ri)

    def __str__(self):
        """Textual representation of a square

        Returns:
            str: description
        """
        return (
            str(self.xcoord)
            + ","
            + str(self.ycoord)
            + " "
            + "Snake: "
            + str(self.snake)
            + " "
            + "Food: "
            + str(self.food)
        )
