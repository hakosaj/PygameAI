import sys
import os
import random
import time
import pygame
import math
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller
from grid import *
from configurations import *

"""Key events for the game
"""

def upKey(xCur, yCur, offset, g, currentOne, currentColor):
    """Press of the up arrow key. Changes the orientation of the block, if
    grid allows for it

    Args:
        xCur (int): current x-coordinate
        yCur (int): current y-coordinate
        offset (int): current offset from the default position
        g (Grid): game grid
        currentOne (Block): current block
        currentColor (Pygame.color): pygame color

    Returns:
        int, int, Block, pygame.Color, bool, Grid, int: Grid state after the operations
    """

    if currentOne == "l":
        if not ((offset == 2 and xCur > 12) or (offset == 6 and xCur > 13)):
            if createConfiguration(xCur, yCur, offset + 2, g, currentOne):
                offset += 2
            else:
                createConfiguration(xCur, yCur, offset, g, currentOne)

    else:
        if currentOne != "o":
            if createConfiguration(xCur, yCur, offset + 2, g, currentOne):
                offset += 2
            else:
                createConfiguration(xCur, yCur, offset, g, currentOne)
    return xCur, yCur, currentOne, currentColor, False, g, offset


def rightKey(xCur, yCur, offset, g, currentOne, currentColor):
    """Press of the right arrow keys. Moves the block to the right, if grid allows.

    Args:
        xCur (int): current x-coordinate
        yCur (int): current y-coordinate
        offset (int): current offset from the default position
        g (Grid): game grid
        currentOne (Block): current block
        currentColor (Pygame.color): pygame color

    Returns:
        int, int, Block, pygame.Color, bool, Grid, int: Grid state after the operation
    """
    if createConfiguration(xCur + 1, yCur, offset, g, currentOne):
        xCur += 1
    else:
        createConfiguration(xCur, yCur, offset, g, currentOne)
    return xCur, yCur, currentOne, currentColor, False, g, offset


def leftKey(xCur, yCur, offset, g, currentOne, currentColor):
    """Press of the left arrow key. Moves block to the left, if grid allows for it

    Args:
        xCur (int): current x-coordinate
        yCur (int): current y-coordinate
        offset (int): current offset from the default position
        g (Grid): game grid
        currentOne (Block): current block
        currentColor (Pygame.color): pygame color

    Returns:
        int, int, Block, pygame.Color, bool, Grid, int: Grid state after the operations
    """
    if createConfiguration(xCur - 1, yCur, offset, g, currentOne):
        xCur -= 1
    else:
        createConfiguration(xCur, yCur, offset, g, currentOne)
    return xCur, yCur, currentOne, currentColor, False, g, offset


def downKey(xCur, yCur, offset, g, currentOne, currentColor, manual):
    """Press of the down arrow key. Moves block down, if grid allows for it.

    Args:
        xCur (int): current x-coordinate
        yCur (int): current y-coordinate
        offset (int): current offset from the default position
        g (Grid): game grid
        currentOne (Block): current block
        currentColor (Pygame.color): pygame color

    Returns:
        int, int, Block, pygame.Color, bool, Grid, int: Grid state after the operations
    """
    if createConfiguration(xCur, yCur + 1, offset, g, currentOne):
        yCur += 1
        return xCur, yCur, currentOne, currentColor, False, g, offset
    else:
        rets = g.spawnBlock(xCur, yCur, offset, g, currentOne, currentColor, manual)
        createConfiguration(rets[0], rets[1], rets[6], rets[5], rets[2])
        return rets


def spaceKey(xCur, yCur, offset, g, currentOne, currentColor, manual):
    """Press of the space key. Drops the block straight down for as far as it goes,
    then spawns a new block.

    Args:
        xCur (int): current x-coordinate
        yCur (int): current y-coordinate
        offset (int): current offset from the default position
        g (Grid): game grid
        currentOne (Block): current block
        currentColor (Pygame.color): pygame color
        manual (bool): manual or auto

    Returns:
        int, int, int, Grid, Block, pygame.Color, block: Grid state after the operations
    """
    while createConfiguration(xCur, yCur + 1, offset, g, currentOne):
        yCur += 1
    rets = g.spawnBlock(xCur, yCur, offset, g, currentOne, currentColor, manual)
    createConfiguration(rets[0], rets[1], rets[6], rets[5], rets[2])
    return rets
