import numpy as np
import random 
import math

def rounddown(x):
    return int(math.ceil(x / 1.0)) * 1

gameCounter = 9
nCol = 5

totals = [rounddown(gameCounter/3)] 
nums = []
for i in totals:
    if i == 0: 
        nums.append([0 for i in range(5)])
        continue
    total = i
    temp = []
    for i in range(4):
        val = np.random.randint(0, total)
        temp.append(val)
        total -= val
    temp.append(total)
    nums.append(temp)
print(nums)
