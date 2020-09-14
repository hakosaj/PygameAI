import sys
import os
import random
import time
import pygame
import math
import copy
from keyEvents import *

class Aiagent:

    def __init__(self):
        self.maxscore=0
        #1 up, 2 right, 3 left
        self.actions=[]


    def clearActions(self):
        self.actions.empty()


    def takeAction(self):
        if (len(self.actions)>0):
            return self.actions.pop(0)
        return -1


    def takeActions(self,keyboard):
        for item in self.actions:
            if item==1:
                keyboard.press(Key.up)
            elif item==2:
                keyboard.press(Key.right)
            else:
                keyboard.press(Key.left)
        self.clearActions()



    def calculateMovement(self, xCur,yCur,currentOne,currentColor,flag,grid,offset):
        #xCur,yCur, currentOne, currentColor, True, grid,offset
        #Alkutilanne
        #def upKey(xCur,yCur,offset,g,currentOne,currentColor):


        params=[xCur,yCur,currentOne,currentColor,flag,grid,offset]
        startState=copy.copy(params)
        #Käydään läpi jokainen actionsekvenssi
        #grid.printGrid()
        moves=-4
        params[5].printGrid()
        for rotate in range(3):
            params=upKey(params[0],params[1],params[6],params[5],params[2],params[3])
        if (moves<0):
            for move in range (abs(moves)):
                params=leftKey(params[0],params[1],params[6],params[5],params[2],params[3])
        else:
            for move in range (abs(moves)):
                params=rightKey(params[0],params[1],params[6],params[5],params[2],params[3])
        rar=params[1]
        while createConfiguration(params[0],rar+1,params[6],params[5],params[2]):
            rar=rar+1
        params=[params[0],rar,params[2],params[3],params[4],params[5],params[6]]
        createConfiguration(params[0],params[1],params[6],params[5],params[2])
        #params[5].printGrid()

        pygame.quit()
        sys.exit()
        
        #for rotates in range(4):
         #   for move in range (-7,8,1):
                #Tehdään kaikki actionit, mikä state sen jälkeen?
                
                



