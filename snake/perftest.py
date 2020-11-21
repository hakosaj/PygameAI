import snake
import matplotlib.pyplot as plt
from pandas import DataFrame
import concurrent.futures
from constants import *
from autosnake import game
from itertools import repeat
import time
import cProfile



pr = cProfile.Profile()
pr.enable()

print("Game with the orientation failsafe")
scores=[]

start=time.time()

iss = [x for x in range(iterations)]

if multi:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for s in executor.map(game,repeat("bfs"),iss):
            scores.append(s)
else:
    for i in range(iterations):

        scores.append(game("bfs"))

print(f"Time: {time.time()-start}")


ta=plt.bar(iss,scores,width=0.8)
datf=DataFrame(scores)
#print(datf.describe())
#plt.show()

pr.disable()
pr.print_stats(sort='time')