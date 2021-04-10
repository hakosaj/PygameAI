import pygame
import math
from breakconstants import *

"""Ball class for the breakout game, sprites and coordinates and moving
"""


class Ball:
    def __init__(self, ballRadius):
        """Initialize the ball object

        Args:
            ballRadius (float): blall radius
        """
        self.x = startX
        self.y = startY
        self.xv = 0
        self.yv = ballVelocity  # self.yv=ballVelocity
        self.radius = ballRadius
        self.circ = pygame.Rect(self.x, self.y, self.radius, self.radius)

    def centerX(self):
        """Retrieve ball center x coordinate

        Returns:
            int: x coordinate
        """
        return self.x + 0.5 * self.radius

    def centerY(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.y + 0.5 * self.radius

    def move_ball(self):
        """Moves the ball object based on currenct velocity, bouncing off walls without loss of momentum"""
        # if (self.y-self.radius>0 and self.y+self.radius+<height-60):
        if self.y - self.radius > 0:
            self.y += self.yv
        else:
            self.yv = -self.yv
            self.y += self.yv

        if self.x - self.radius > 0 and self.x + self.radius < width:
            self.x += self.xv
        else:
            self.xv = -self.xv
            self.x += self.xv

    def draw_ball(self):
        """Draw the ball sprites"""
        self.circ = pygame.Rect(self.x, self.y, self.radius, self.radius)
        pygame.draw.circle(
            screen, BLACK, (round(self.x), round(self.y)), self.radius + 2
        )
        pygame.draw.circle(screen, WHITE, (round(self.x), round(self.y)), self.radius)
