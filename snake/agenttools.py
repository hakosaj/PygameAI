import sys
import os
import random
import time
import pygame
import math
from snek import Snek
from constants import *
from pygame.locals import *
from pynput.keyboard import Key, Controller
from grid import *
from collections import deque,defaultdict
from collections import defaultdict, deque




#Take action based on the current snake and list of movements that need to be done
def takeAction(orientations, s):

    #While cannot change,take random, mean 60
    #ore=0
    #tried=0
    #tries=len(orientations)*2
    #while not s.changeOrientation(orientations[ore]):
    #    ore = random.randrange(len(orientations))
    #    tried+=1
    #    if (tried==tries):
    #        s.changeOrientation(orientations[ore])
    #        break
    #orientations.pop(ore)
    #return orientations

    #While cannot change, take last , mean 60 but fastest
    if not s.changeOrientation(orientations[0]):
        orientations=orientations[::-1]
        s.changeOrientation(orientations[0])
    return orientations[1:]


    #Just always taje the correct one, mean 36
    #s.changeOrientation(orientations[0])
    #return orientations[1:]


#BFS, dont take moving snake into account. 
def bfs(g,s):
    #Visited
    visited=[[False] * g.x0 for i in range(g.y0)]
    parents=[[-1]*g.x0 for i in range(g.y0)]
    #Queue for the bfs, append the head of the snake
    de = deque([])
    de.append(s.squares[0])
    #print(f"Snake at {s.squares[0].xcoord},{s.squares[0].ycoord}")
    a=0
    while de:
        #dequeue
        cur = de.popleft()
        if cur.food:
            if (prints):
                print(f"food found at {cur.xcoord},{cur.ycoord}")
            break
        #Add to visiteds
        visited[cur.xcoord][cur.ycoord]=True
        #print(cur)
        #print(a)
        #a+=1
        #Add all neighbors to queue, end of it so bfs (dfs would be top of it)
        #Add only if not visited and not snake, also returns None if out of bounds:

        
        #Parent states the orientation what was taken to reach it
        nb = g.neighborAt(cur,0)
        if (nb!=None and (not nb.snake) and (not visited[nb.xcoord][nb.ycoord])):
            de.append(nb)
            visited[nb.xcoord][nb.ycoord]=True
            parents[nb.xcoord][nb.ycoord]=0

        nb = g.neighborAt(cur,2)
        if (nb!=None and (not nb.snake) and (not visited[nb.xcoord][nb.ycoord])):
            de.append(nb)
            visited[nb.xcoord][nb.ycoord]=True
            parents[nb.xcoord][nb.ycoord]=2

        nb = g.neighborAt(cur,4)
        if (nb!=None and (not nb.snake) and (not visited[nb.xcoord][nb.ycoord])):
            de.append(nb)
            visited[nb.xcoord][nb.ycoord]=True
            parents[nb.xcoord][nb.ycoord]=4

        nb = g.neighborAt(cur,6)
        if (nb!=None and (not nb.snake) and (not visited[nb.xcoord][nb.ycoord])):
            de.append(nb)
            visited[nb.xcoord][nb.ycoord]=True
            parents[nb.xcoord][nb.ycoord]=6

    #Print grid orientations
    #for bd in parents:
    #    for item in bd:
    #        print(" ",item, end='')
    #    print("\n")

    orientations=[]
    while (parents[cur.xcoord][cur.ycoord]!=-1 ):
        #print(f"x and y: {cur.xcoord} {cur.ycoord} and parent orientation: {parents[cur.xcoord][cur.ycoord]}")
        orientations.append(parents[cur.xcoord][cur.ycoord])
        cur=g.neighborAt(cur,(parents[cur.xcoord][cur.ycoord]+4)%8)

    if prints:
        for item in orientations:
            print(item, end='')
        print("\n")

    orientations.reverse()
    return orientations


