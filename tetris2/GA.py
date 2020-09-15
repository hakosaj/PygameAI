import sys
import os
import random
import time
import pygame
import math
from itertools import combinations
import pickle
from constants import *
from tetris import *


#Population size
#Real: 100
popsize=100
a=-2
b=2
maxBlocks=500
generations=4
survivalRate=0.4

        #ax = self.a*g.totalHeight()
        #bx = self.b*g.virtualFullRows()
        #cx = self.c*g.holes()
        #dx = self.d*g.bumpiness()


#Initialize generation
parents=[]
for i in range(popsize):
    parents.append([random.uniform(a, b),random.uniform(a, b),random.uniform(a, b),random.uniform(a, b)])





#Run GA here
for i in range(generations):
    print(f"Generation {i}")


    #Fitness test: play the game
    fitnesses=[]
    for i in range(len(parents)):
        fitness=game(parents[i],i,popsize,maxBlocks,i,generations)
        fitnesses.append((i,fitness,parents[i]))




    #Save fitnesses
    name='generation'+str(generation)+'.dump'
    pickle.dump(fitnesses, open(name, 'wb'))
    fitnesses = pickle.load(open(name, 'rb'))

    #If you wanna load something already there:
    #fitnesses=pickle.load(open('tuple.dump','rb'))

    fitnesses.sort(key=lambda x:x[1],reverse=True)
    avga=0
    avgb=0
    avgc=0
    avgd=0
    for item in fitnesses:
        avga+=item[0]
        avgb+=item[1]
        avgc+=item[2]
        avgd+=item[3]
    print(f"newgen: avg a: {avga/popsize} and avgb: {avgb/popsize} \n and avgc: {avgc/popsize} and avgd: {avgd/popsize}")
    parents=newgen

    #Tournament selection: first choose 20% of population at random(10 individuals)
    #Of these choose the two with the best finesses and save them to newParents-list
    #Repeat until 40% of the old pop is chosen. eg. 20

    newParents=[]
    while len(newParents)<popsize*survivalRate:
        best = random.sample(fitnesses,int((popsize*survivalRate)/2.0))
        best.sort(key=lambda x:x[1],reverse=True)
        if (best[0] not in newParents):
            newParents.append(best[0])
        if (best[1] not in newParents):
            newParents.append(best[1])

    #print("\n And here's the chosen new parents:")
    #for item in newParents:
        #print(item)

    #Weighted average crossover: 
    newgen=[]
    #Choose random integer pairs
    pairs=random.sample(list(combinations(range(40),2)),100)
    for item in pairs:
        #Get the parents from newParents-list
        parent1=newParents[item[0]]
        parent2=newParents[item[1]]
        fit1=parent1[1]+1
        fit2=parent2[1]+1
        normalizeConstant = fit1+fit2
        normf1=fit1/normalizeConstant
        normf2=fit2/normalizeConstant
        vector1=parent1[2]
        vector2=parent2[2]
        newa = vector1[0]*normf1+vector2[0]*normf2
        newb = vector1[1]*normf1+vector2[1]*normf2
        newc = vector1[2]*normf1+vector2[2]*normf2
        newd = vector1[3]*normf1+vector2[3]*normf2
        weightvector=[newa,newb,newc,newd]
        #print(f"Vectors {vector1} and \n        {vector2} result in\n        {weightvector} \n with fitnesses {fit1} and {fit2}")
        newgen.append(weightvector)
        #print(weightvector)


    for item in newgen:
        avga+=item[0]
        avgb+=item[1]
        avgc+=item[2]
        avgd+=item[3]
    print(f"newgen: avg a: {avga/popsize} and avgb: {avgb/popsize} \n and avgc: {avgc/popsize} and avgd: {avgd/popsize}")
    parents=newgen