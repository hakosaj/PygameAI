import sys
import os
import random
import time
import pygame
import math
import copy
import itertools
import multiprocessing 
from itertools import repeat
from keyEvents import *

class Aiagent:

    def __init__(self,weights):
        #1 up, 2 right, 3 left
        self.actions=[]
        self.a=weights[0]
        self.b=weights[1]
        self.c=weights[2]
        self.d=weights[3]


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
        a,b,c,d=g.totalScoring()
        ax = self.a*a
        bx = self.b*b
        cx = self.c*c
        dx = self.d*d
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


    def virtualMovementMP(self,xCur,yCur,currentOne,currentColor,flag,grid,offset,moves,rotation):
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
        return (moves, rotation, scor)

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

        
        start=time.time()
        
        #rots=[0,1,2,3]
        #mvs=[-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
        #c = list(itertools.product(rots,mvs))
        #c= [list(elem) for elem in c]
        #c=list(map(lambda x: copy.deepcopy(startState)+x,c))
        #with multiprocessing.Pool(processes=2) as pool:
        #    sets = pool.starmap(self.virtualMovementMP,c)
        
        for rotates in range(4):
           for move in range (-7,8,1):
               score=self.virtualMovement(*params,move,rotates)
               params=startState
               if score>maxscore:
                   maxscore=score
                   maxmove=move
                   maxrotate=rotates

        #maxelement= max(sets, key=lambda x:x[2])
        #maxrotateMP=maxelement[1]
        #maxmoveMP=maxelement[0]
        #print(f"Normal max rotates: {maxrotate} and MP: {maxrotateMP}")
        #print(f"Normal max moves: {maxmove} and MP: {maxmoveMP}")

        print(f"Virtual move time: {time.time()-start}")


        self.addAction(1,maxrotate)
        if (maxmove<0):
            self.addAction(3,abs(maxmove))
        elif (maxmove>0):
            self.addAction(2,abs(maxmove))

        #for item in self.actions:
        #    print(item)
        


                
                
                



