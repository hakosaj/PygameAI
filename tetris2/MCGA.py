import sys
import os
import random
import time
import pygame
import copy
import math
import concurrent.futures
from itertools import combinations
import pickle
from constants import *
from tetrisNonvisual import game
from itertools import repeat


    """Multicore nonvisual genetic algorithm for playing the game,
    and for finding optimal parameters.
    """

# Population size
# Real: 100
popsize = 100
a = -2
b = 2
maxBlocks = 500
generations = 7
mutationChance = 0.1
survivalRate = 0.4


# Initialize generation
parents = []
newgen = []
for i in range(popsize):
    parents.append(
        [
            random.uniform(a, 0),
            random.uniform(0, b),
            random.uniform(a, 0),
            random.uniform(a, 0),
        ]
    )


# Run GA here
pted = False
loaded = True
for g in range(generations):
    print(f"Generation {g}")

    nts = [x for x in range(popsize)]

    # Print MPC info
    if not pted:
        print(f"Starting Tetris GA with {os.cpu_count()} parallel processes.")
        pted = True

    fitnesses = []
    if not loaded:
        fitnesses = pickle.load(open("generation1.dump", "rb"))
        loaded = True
    else:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for a, fit, pt in executor.map(
                game,
                parents,
                nts,
                repeat(popsize),
                repeat(maxBlocks),
                repeat(g),
                repeat(generations),
                repeat(False),
                repeat(True),
            ):
                fitnesses.append((a, fit, pt))

    # for i in range(len(parents)):
    # fitness=game(parents[i],i,popsize,maxBlocks,g,generations,False,True)
    # fitnesses.append((i,fitness,parents[i]))
    # print(f"Done {i}/{len(parents)}")

    # Save fitnesses
    name = "generation" + str(g) + ".dump"
    pickle.dump(fitnesses, open(name, "wb"))

    # load
    fitnesses = pickle.load(open(name, "rb"))
    # fitnesses = pickle.load(open('generation1.dump', 'rb'))
    print(len(fitnesses))

    fitnesses.sort(key=lambda x: x[1], reverse=True)
    avga = 0
    avgb = 0
    avgc = 0
    avgd = 0
    avgfit = 0
    for item in fitnesses:
        avga += item[2][0]
        avgb += item[2][1]
        avgc += item[2][2]
        avgd += item[2][3]
        avgfit += item[1]
    print(
        f"newgen:avgfitness: {avgfit/popsize} avg a: {avga/popsize} and avgb: {avgb/popsize} \n and avgc: {avgc/popsize} and avgd: {avgd/popsize}"
    )
    print(f"Best fit parent: {fitnesses[0][1]} with abcd: {fitnesses[0][2]}")
    # Tournament selection: first choose 20% of population at random(10 individuals)
    # Of these choose the two with the best finesses and save them to newParents-list
    # Repeat until 40% of the old pop is chosen. eg. 20
    newParents = []
    tfits = copy.deepcopy(fitnesses)
    print("Tournament selection baby")
    while len(newParents) < popsize * survivalRate:
        # best = random.sample(fitnesses,int((popsize*survivalRate)))
        best = random.sample(tfits, int((popsize * survivalRate)))
        best.sort(key=lambda x: x[1], reverse=True)
        if best[0] not in newParents:
            newParents.append(best[0])
            tfits.remove(best[0])
        if best[1] not in newParents:
            newParents.append(best[1])
            tfits.remove(best[1])

    # print("\n And here's the chosen new parents:")
    # for item in newParents:
    # print(item)

    # Weighted average crossover:
    # Choose random integer pairs
    pairs = random.sample(
        list(combinations(range(int(popsize * survivalRate)), 2)), int(popsize)
    )
    for item in pairs:
        # Get the parents from newParents-list
        parent1 = newParents[item[0]]
        parent2 = newParents[item[1]]
        fit1 = parent1[1] + 1
        fit2 = parent2[1] + 1
        normalizeConstant = fit1 + fit2
        normf1 = fit1 / normalizeConstant
        normf2 = fit2 / normalizeConstant
        vector1 = parent1[2]
        vector2 = parent2[2]
        newa = vector1[0] * normf1 + vector2[0] * normf2
        newb = vector1[1] * normf1 + vector2[1] * normf2
        newc = vector1[2] * normf1 + vector2[2] * normf2
        newd = vector1[3] * normf1 + vector2[3] * normf2
        weightvector = [newa, newb, newc, newd]
        # print(f"Vectors {vector1} and \n        {vector2} result in\n        {weightvector} \n with fitnesses {fit1} and {fit2}")
        newgen.append(weightvector)
        # print(weightvector)

    # Mutation
    for item in newgen:
        if random.random() > 0.9:
            toMutate = random.randint(0, 3)
            if random.random() > 0.5:
                item[toMutate] = item[toMutate] + 0.2
            else:
                item[toMutate] = item[toMutate] - 0.2

    for item in newgen:
        avga += item[0]
        avgb += item[1]
        avgc += item[2]
        avgd += item[3]
    print(
        f"newgen: avg a: {avga/popsize} and avgb: {avgb/popsize} \n and avgc: {avgc/popsize} and avgd: {avgd/popsize} n \n \n"
    )
    parents = newgen
    newgen = []
    popsize -= 10
    maxBlocks += 300 * (1 + g)
