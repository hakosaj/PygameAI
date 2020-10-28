import autosnake
import matplotlib.pyplot as plt
from constants import *
from pandas import DataFrame
import concurrent.futures
import time




print("Game with the orientation failsafe")
scores=[]
iss = [x for x in range(1000)]

start=time.time()

if multi:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for s in executor.map(autosnake.game,iss):
            scores.append(s)
else:
    for i in range(200):
        scores.append(autosnake.game())

print(f"Time: {time.time()-start}")


ta=plt.bar(iss,scores,width=0.8)
datf=DataFrame(scores)
print(datf.describe())
plt.show()
