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
scores = []
iss = [x for x in range(iterations)]

start = time.time()

if multi:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for s in executor.map(game,repeat("hamiltonian"),iss):
            scores.append(s)
else:
    for i in range(iterations):

        scores.append(game("hamiltonian"))

print(f"Time: {time.time()-start}")


scores.sort()
filtered=list(filter(lambda x:x>10,scores))
ta=plt.hist(scores,bins=20)
stata, ps = stats.shapiro(filtered)
stat, p = stats.shapiro(scores)
print(f"for filtered, p is {ps} versus 0.05 \n")
print(f"p is {p} versus 0.05")
if p > 0.05:
    print("Gaussian")
else:
    print("Not gaussian")



datf=DataFrame(scores)
print(datf.describe())
plt.show()
