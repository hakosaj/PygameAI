import snake
import matplotlib.pyplot as plt
from pandas import DataFrame
import concurrent.futures
import time
import cProfile


pr = cProfile.Profile()
pr.enable()

print("Game with the orientation failsafe")
scores = []
iss = [x for x in range(20)]

start = time.time()

# with concurrent.futures.ProcessPoolExecutor() as executor:
#    for s in executor.map(snake.game,iss):
#        scores.append(s)
for i in range(20):
    scores.append(snake.game())

print(f"Time: {time.time()-start}")


ta = plt.bar(iss, scores, width=0.8)
datf = DataFrame(scores)
# print(datf.describe())
# plt.show()

pr.disable()
pr.print_stats(sort="time")
