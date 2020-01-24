import random
import numpy as np


# function to generate random numbers given specific weights
def weighted_random(values, weights):
    total_weight = sum(weights)
    acum_weights = [w / total_weight for w in weights[:]]
    for i in range(len(weights)-1):
        acum_weights[i+1] += acum_weights[i]
    rand = random.random()
    for value, weight in zip(values, acum_weights):
        if weight > rand:
            return value


# testing function
arr = []
for i in range(10000):
    arr.append(weighted_random([1,2,3],[0.5,0.3,0.2]))

freq = np.divide([arr.count(i) for i in np.unique(arr)],10000)
print(freq)
