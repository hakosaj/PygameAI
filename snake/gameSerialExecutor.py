from autosnake import game
import matplotlib.pyplot as plt
from constants import *
from pandas import DataFrame
import concurrent.futures
from itertools import repeat
import time




print("Game with the orientation failsafe")
scores=[]
iss = [x for x in range(100)]

start=time.time()

if multi:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for s in executor.map(game,repeat("bfs"),iss):
            scores.append(s)
else:
    for i in range(20):
        scores.append(game("longest"))

print(f"Time: {time.time()-start}")


ta=plt.bar(iss,scores,width=0.8)
datf=DataFrame(scores)
print(datf.describe())
plt.show()
