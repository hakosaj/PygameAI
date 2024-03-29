import sys
import os
import random
import time
import pygame
import math
from snek import Snek
from constants import *
from pygame.locals import *
from grid import *
from agenttools import (
    bfs,
    takeAction,
    dfs,
    longestPath,
    hamiltonianPath,
    hamiltonianPathShortcuts,
)
import cProfile


def game(algorithm, t=2):
    """Actual game function

    Args:
        algorithm (string): algorithm of choice
        t (int, optional): Defaults to 2.

    Returns:
        Integer: score
    """

    # Tetris grid, true as last argument if walls
    g = Grid(gridsizex, gridsizey, walls)

    # Screen objects
    g.createSquares()
    snek = Snek(
        random.randrange(2, gridsizex - 2), random.randrange(2, gridsizey - 2), g
    )
    g.randomFood()

    score = 0
    # Initialize pygame
    if visualized:
        pygame.init()
        pygame.font.init()
        # Fonts and gavkground
        scorefont = pygame.font.SysFont("Comic Sans MS", 40)
        gameoverfont = pygame.font.SysFont("Comic Sans MS", 40)
        algofont = pygame.font.SysFont("Arial", 20)

    orientations = []

    start_time = None
    clock = pygame.time.Clock()

    foodEaten = True

    tickcounter = 0

    while not snek.dead:
        if visualized:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pygame.event.clear()
                        event = pygame.event.wait()
                        while event.key != pygame.K_o:
                            pygame.event.clear()
                            event = pygame.event.wait()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    elif event.key == pygame.K_RIGHT:
                        snek.changeOrientation(2)
                    elif event.key == pygame.K_DOWN:
                        snek.changeOrientation(4)
                    elif event.key == pygame.K_LEFT:
                        snek.changeOrientation(6)
                    elif event.key == pygame.K_UP:
                        snek.changeOrientation(0)

                    elif event.key == pygame.K_r:
                        g.printGrid()

        if foodEaten:
            g.clearPath()
            if algorithm == "bfs":
                orientations = bfs(g, snek.hed())
            elif algorithm == "dfs":
                orientations = dfs(g, snek.hed())
            elif algorithm == "longest":
                orientations = longestPath(g, snek)
            elif algorithm == "hamiltonian":
                if snek.length() >= 3:
                    orientations = hamiltonianPath(g, snek)
                else:
                    orientations = bfs(g, snek.hed())
            if paths:
                g.colorPath(snek, orientations)
            foodEaten = False

        if len(orientations) > 0:
            orientations = takeAction(orientations, snek)

        if snek.moveSnake():
            foodEaten = True
            score += 1

        if visualized:
            g.drawGrid()

        tickcounter += 1
        if visualized:
            pygame.display.flip()
            clock.tick(fps)

    print(f"Score: {score}")
    return score


def main():
    game("hamiltonian")


main()
