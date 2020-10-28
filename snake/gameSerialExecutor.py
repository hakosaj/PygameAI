import autosnake
import matplotlib.pyplot as plt
from constants import *
from pandas import DataFrame
import concurrent.futures
import time




print("Game with the orientation failsafe")
scores=[]
iss = [x for x in range(200)]

start=time.time()

if multi:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for s in executor.map(snake.game,iss):
            scores.append(s)
else:
    for i in range(200):
        scores.append(snake.game())

print(f"Time: {time.time()-start}")


ta=plt.bar(iss,scores,width=0.8)
datf=DataFrame(scores)
#print(datf.describe())
#plt.show()
