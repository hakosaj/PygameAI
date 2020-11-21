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



def bfsTarget(g,s,target,visited):
    #visited=[[False] * g.x0 for i in range(g.y0)]
    parents=[[-1]*g.x0 for i in range(g.y0)]
    print(f"current: {s.xcoord},{s.ycoord}")
    print(f"target: {target.xcoord},{target.ycoord}")

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


        a= [0,2,4,6]
        for item in a:
            nb=g.neighborAt(cur,item)
            if firstPass:
                if ( nb!=None and (not nb.snake) and (not (nb.food)) and (not visited[nb.xcoord][nb.ycoord])):
                    de.append(nb)
                    visited[nb.xcoord][nb.ycoord]=True
                    parents[nb.xcoord][nb.ycoord]=item
            else:
                if ( (nb==target)):
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
        #print(f"New path: target = {target.xcoord},{target.ycoord}, current = {s.xcoord},{s.ycoord}")
        #for item in orientations:
        #    print(item, end='')
        #print("\n")
        return orientations
    else:
        return None

def bfsTarget2(g,s,target,visited):
    #Visited
    parents=[[-1]*g.x0 for i in range(g.y0)]
    #print(f"current: {s.xcoord},{s.ycoord}")
    #print(f"target: {target.xcoord},{target.ycoord}")

    #Queue for the bfs, append the head of the snake
    de = deque([])
    de.append(s)
    #print(f"Snake at {s.squares[0].xcoord},{s.squares[0].ycoord}")
    a=0
    while de:
        #dequeue
        cur = de.popleft()
        #Add to visiteds
        if cur.xcoord==target.xcoord and cur.ycoord==target.ycoord:
            #print("target found")
            found=True
            break
        visited[cur.xcoord][cur.ycoord]=True

        a= [0,2,4,6]
        for item in a:
            nb=g.neighborAt(cur,item)
            if (nb!=None and (not visited[nb.xcoord][nb.ycoord])):
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


def hamiltonianPath(g,s):
    #Generate longest path from head to last square of snake
    #Every snake body square but first and last is already 
    #and thus not legal. Only if length is larger than 3
    visited=[[False] * g.x0 for i in range(g.y0)]
    body = s.body()
    for item in body:
        visited[item.xcoord][item.ycoord]=True
    target =s.tail()
    orientations = bfsTarget2(g,s.hed(),target,visited)
    #Orientations: bfs from head to tail, not crossing the snake itself
    #Next: create a longest path
    #sys.exit()

    visited=[[False] * g.x0 for i in range(g.y0)]
    body = s.body()
    for item in body:
        visited[item.xcoord][item.ycoord]=True
    
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
            ##If not snake, or illegal:
            if (thistest!=None and not visited[thistest.xcoord][thistest.ycoord]):
                if (nexttest!=None  and not visited[nexttest.xcoord][nexttest.ycoord]):
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


def relative_dist(self, ori, x, size):
    if ori > x:
        x += size
    return x - ori

def hamiltonianPathShortcuts(g,s):
    #Generate longest path from head to last square of snake
    #Every snake body square but first and last is already 
    #and thus not legal. Only if length is larger than 3
    visited=[[False] * g.x0 for i in range(g.y0)]
    body = s.body()
    for item in body:
        visited[item.xcoord][item.ycoord]=True
    target =s.tail()
    orientations = bfsTarget2(g,s.hed(),target,visited)
    #Orientations: bfs from head to tail, not crossing the snake itself
    #Next: create a longest path
    #sys.exit()

    visited=[[False] * g.x0 for i in range(g.y0)]
    body = s.body()
    for item in body:
        visited[item.xcoord][item.ycoord]=True
    
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
            ##If not snake, or illegal:
            if (thistest!=None and not visited[thistest.xcoord][thistest.ycoord]):
                if (nexttest!=None  and not visited[nexttest.xcoord][nexttest.ycoord]):
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


    #Shortcut time
    cnt=1
    s.resetIndexTable()
    for item in makePathFromOrientations(orientations,s.hed(),g):
        s.indexTable[item.xcoord][item.ycoord]=cnt
        cnt+=1



    #Only shurtcut if snake length is small
    if s.length()<0.5*gridsizex*gridsizey:
        realPath=makePathFromOrientations(orientations,s.hed(),g)
        path = bfs(g,s.hed())
        tail=s.tail()
        head=s.hed()
        direction = orientations[0]
        following = g.neighborAt(cur,direction)
        food=g.foodsquare
        tailindex = s.indexTable[tail.xcoord][tail.ycoord]
        headindex = s.indexTable[head.xcoord][head.ycoord]
        nextindex = s.indexTable[following.xcoord][following.ycoord]
        foodindex = s.indexTable[food.xcoord][food.ycoord]

        if not (len(path)==1) and abs(foodindex-tailindex)==1:

            headrelative = self.relative_dist(tailindex, headindex, gridsizex*gridsizey)
            nextrelative= self.relative_dist(tailindex, nextindex, gridsizex.gridsize)
            foodrelative = self.relative_dist(tailindex, foodindex, gridsizex*gridsizey)
            if nextrelative > headrelative and nextrelative <= foodrelative:
                #This means we'll mofdify the orientations-one: remove
                #from realPath head till ath[0] is found
                tfind=realPath[0]
                removed=0
                while (tfind.xcoord!=path[0].xcoord and tfind.ycoord!=path[0].ycoord):
                    realPath.pop[0]
                    tfind=realPath[0]
                    removed+=1
                print(removed)
                sys.exit()

                nxt_direc = path[0]

    return nxt_direc



    sys.exit()

    return orientations
