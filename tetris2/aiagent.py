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
        #1 up, 2 right, 3 left
        self.actions=[]
        self.a=-0.5
        self.b=0.9
        self.c=-0.4
        self.d=-0.2


    def clearActions(self):
        self.actions=[]


    def takeAction(self):
        if (len(self.actions)>0):
            return self.actions.pop(0)
        return -1

    def addAction(self,action,amount):
        for i in range(amount):
            self.actions.append(action)




    def calculateScore(self,g):
        ax = self.a*g.totalHeight()
        bx = self.b*g.virtualFullRows()
        cx = self.c*g.holes()
        dx = self.d*g.bumpiness()
        return ax+bx+cx+dx


    def virtualMovement(self,xCur,yCur,currentOne,currentColor,flag,grid,offset,moves,rotation):
        params=[xCur,yCur,currentOne,currentColor,flag,grid,offset]
        for rotate in range(rotation):
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

        changedSquares=[]
        for item in params[5].squares:
            for sq in item:
                if sq.status==2:
                    params[5].forceChangeStatus(sq,1)
                    changedSquares.append(sq)

        #params[5].printGrid()
        scor= self.calculateScore(params[5])
        for item in changedSquares:
            params[5].forceChangeStatus(item,2)
        return scor


    def calculateMovement(self, xCur,yCur,currentOne,currentColor,flag,grid,offset):
        self.clearActions()
        #xCur,yCur, currentOne, currentColor, True, grid,offset
        #Alkutilanne
        #def upKey(xCur,yCur,offset,g,currentOne,currentColor):
        #1 up, 2 right, 3 left
        maxscore=-9999999999
        maxrotate=0
        maxmove=0
        params=[xCur,yCur,currentOne,currentColor,flag,grid,offset]
        startState=copy.deepcopy(params)

        
        for rotates in range(4):
           for move in range (-7,8,1):
               score=self.virtualMovement(*params,move,rotates)
               params=startState
               #print(score)
               if score>maxscore:
                   maxscore=score
                   maxmove=move
                   maxrotate=rotates

        #print(f"{maxrotate} rotations and {maxmove} movement")
        self.addAction(1,maxrotate)
        if (maxmove<0):
            self.addAction(3,abs(maxmove))
        elif (maxmove>0):
            self.addAction(2,abs(maxmove))

        #for item in self.actions:
        #    print(item)
        


                
                
                



