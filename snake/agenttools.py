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

    #While cannot change,take random, mean 73,77s
    #ore=0
    #tried=0
    #tries=len(orientations)
    #while not s.changeOrientation(orientations[ore]):
    #    ore = random.randrange(len(orientations))
    #    tried+=1
    #    if (tried==tries):
    #        s.changeOrientation(orientations[ore])
    #        break
    #orientations.pop(ore)
    #return orientations

    #While cannot change, take last , mean 74, 80.5s
    if not s.changeOrientation(orientations[0]):
        orientations=orientations[::-1]
        s.changeOrientation(orientations[0])
    return orientations[1:]


    #Just always taje the correct one, mean 36
    #s.changeOrientation(orientations[0])
    #return orientations[1:]

#Targeted BFS
#def bfs(g,s):



def bfsTarget(g,s,path,target):
    visited=[[False] * g.x0 for i in range(g.y0)]
    parents=[[-1]*g.x0 for i in range(g.y0)]

    firstPass=True
    found=False
    de = deque([])
    de.append(s)
    while de:
        cur = de.popleft()
        if cur.xcoord==target.xcoord and cur.ycoord==target.ycoord:
            print("target found")
            found=True
            break
        visited[cur.xcoord][cur.ycoord]=True

        #Ei saa olla pathilla jos firstPass
        #Jos ei first Pass,ei saa olla pathilla paitsi jos target

        a= [0,2,4,6]
        for item in a:
            nb=g.neighborAt(cur,item)
            if firstPass:
                if ((nb not in path) and nb!=None and (not nb.snake) and (not (nb.food)) and (not visited[nb.xcoord][nb.ycoord])):
                    de.append(nb)
                    visited[nb.xcoord][nb.ycoord]=True
                    parents[nb.xcoord][nb.ycoord]=item
            else:
                if ((nb not in path) or (nb==target)):
                    if ( nb!=None and (not nb.food) and (not nb.snake) and (not visited[nb.xcoord][nb.ycoord])):
                        de.append(nb)
                        visited[nb.xcoord][nb.ycoord]=True
                        parents[nb.xcoord][nb.ycoord]=item

        firstPass=False

    if found:
        orientations=[]
        while (parents[cur.xcoord][cur.ycoord]!=-1 ):
            orientations.append((parents[cur.xcoord][cur.ycoord]))
            cur=g.neighborAt(cur,(parents[cur.xcoord][cur.ycoord]+4)%8)

        orientations.reverse()
        print(f"New path: target = {target.xcoord},{target.ycoord}, current = {s.xcoord},{s.ycoord}")
        for item in orientations:
            print(item, end='')
        print("\n")
        return orientations
    else:
        return None


#BFS, dont take moving snake into account. How to take the current orientation into account?
#def bfs(g,s):
def bfs(g,s):
    #Visited
    visited=[[False] * g.x0 for i in range(g.y0)]
    parents=[[-1]*g.x0 for i in range(g.y0)]
    #Queue for the bfs, append the head of the snake
    de = deque([])
    de.append(s)
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

        a= [0,2,4,6]
        for item in a:
            nb=g.neighborAt(cur,item)
            if (nb!=None and (not nb.snake) and (not visited[nb.xcoord][nb.ycoord])):
                de.append(nb)
                visited[nb.xcoord][nb.ycoord]=True
                parents[nb.xcoord][nb.ycoord]=item




    orientations=[]
    while (parents[cur.xcoord][cur.ycoord]!=-1 ):
        #print(f"x and y: {cur.xcoord} {cur.ycoord} and parent orientation: {parents[cur.xcoord][cur.ycoord]}")
        orientations.append(parents[cur.xcoord][cur.ycoord])
        cur=g.neighborAt(cur,(parents[cur.xcoord][cur.ycoord]+4)%8)
    
    #print(f"New path: target = {target.xcoord},{target.ycoord}")
    #for item in orientations:
    #    print(item, end='')
    #print("\n")
    #sys.exit()



    orientations.reverse()
    return orientations



#DFS, dont take moving snake into account. How to take the current orientation into account?
def dfs(g,s):
    #Visited
    visited=[[False] * g.x0 for i in range(g.y0)]
    parents=[[-1]*g.x0 for i in range(g.y0)]
    #Queue for the bfs, append the head of the snake
    de = deque([])
    de.appendleft(s)
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
            de.appendleft(nb)
            visited[nb.xcoord][nb.ycoord]=True
            parents[nb.xcoord][nb.ycoord]=0

        nb = g.neighborAt(cur,2)
        if (nb!=None and (not nb.snake) and (not visited[nb.xcoord][nb.ycoord])):
            de.appendleft(nb)
            visited[nb.xcoord][nb.ycoord]=True
            parents[nb.xcoord][nb.ycoord]=2

        nb = g.neighborAt(cur,4)
        if (nb!=None and (not nb.snake) and (not visited[nb.xcoord][nb.ycoord])):
            de.appendleft(nb)
            visited[nb.xcoord][nb.ycoord]=True
            parents[nb.xcoord][nb.ycoord]=4

        nb = g.neighborAt(cur,6)
        if (nb!=None and (not nb.snake) and (not visited[nb.xcoord][nb.ycoord])):
            de.appendleft(nb)
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




def printPath(path):
    for item in path:
        print(f"({item.xcoord},{item.ycoord})->",end='')
    print("\n")


def makePathFromOrientations(orientations,g,s):
    path=[]
    cur = g.elementAt(s.xcoord,s.ycoord)
    for item in orientations:
        cur = g.neighborAt(cur,(item))
        path.append(cur)
    #path.reverse()
    return path




def longestPath(g,s):
    
    orientations = bfs(g,s.hed())
    visited=[[False] * g.x0 for i in range(g.y0)]
    cur = g.elementAt(s.hed().xcoord,s.hed().ycoord)
    for item in orientations:
        cur = g.neighborAt(cur,item)
        visited[cur.xcoord][cur.ycoord]=True

    if (len(orientations)==0):
        orientations=[s.movement]
        return orientations
    #Extend between each pair of positions
    cur=s.hed()
    i=0
    while 1:
        direction = orientations[i]
        following = g.neighborAt(cur,direction)
        
        if direction==6 or direction==2:
            tests=[0,4]
        elif direction==0 or direction==4:
            tests=[2,6]

        extended=False
        for item in tests:
            thistest=g.neighborAt(cur,item)
            nexttest=g.neighborAt(following,item)
            ##If not snake, food or illegal:
            if (thistest!=None and not thistest.snake and not thistest.food and not visited[thistest.xcoord][thistest.ycoord]):
                if (nexttest!=None and not nexttest.snake and not nexttest.food and not visited[nexttest.xcoord][nexttest.ycoord]):
                    visited[thistest.xcoord][thistest.ycoord]=True
                    visited[nexttest.xcoord][nexttest.ycoord]=True
                    orientations.insert(i,item)
                    orientations.insert(i+2,(item+4)%8)
                    extended=True
                    break
        if not extended:
            cur=following
            i+=1
            if (i>=len(orientations)):
                break

    return orientations

