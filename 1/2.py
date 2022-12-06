# answer = 203420

import heapq as hq

with open("i2.txt") as f:
    calories = f.readlines()

maxs = []
count = 0
for cal in calories:
    if cal == "\n":
        maxs.append(count)
        count = 0
    else:
        count += int(cal)

total = sum(hq.nlargest(3, maxs))
print(total)
