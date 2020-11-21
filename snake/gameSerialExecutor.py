from autosnake import game
import matplotlib.pyplot as plt
from constants import *
from scipy import stats
from pandas import DataFrame
import numpy as np
import concurrent.futures
from statsmodels.graphics.gofplots import qqplot
from itertools import repeat
import time


print("Game with the orientation failsafe")
scores=[]
iss = [x for x in range(iterations)]

start=time.time()

if multi:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for s in executor.map(game,repeat("bfs"),iss):
            scores.append(s)
else:
    for i in range(iterations):

        scores.append(game("bfs"))

print(f"Time: {time.time()-start}")


scores.sort()
#ta=plt.bar(scores,iss,width=0.8)
ta=plt.hist(scores,bins=20)
k2, p = stats.normaltest(scores)
print("p = {:g}".format(p))
datf=DataFrame(scores)
print(datf.describe())
plt.show()
