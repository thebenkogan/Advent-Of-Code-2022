# ans = 2520

import heapq as hq
from math import hypot
import matplotlib.pyplot as plt

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    cubes = [line.strip() for line in f.readlines()]


def dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return hypot(x2 - x1, y2 - y1, z2 - z1)


adjacencies = [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]

positions = set()
for cube in cubes:
    positions.add(tuple([int(n) for n in cube.split(",")]))


max_x, sum_x, sum_y, sum_z = 0, 0, 0, 0
xvals, yvals, zvals = [], [], []
for x, y, z in positions:
    x = max(max_x, x)
    xvals.append(x)
    yvals.append(y)
    zvals.append(z)
    sum_x += x
    sum_y += y
    sum_z += z
avg = (sum_x / len(positions), sum_y / len(positions), sum_z / len(positions))
start = (max_x + 2, 0, 0)

frontier = [(dist(start, avg), start)]
seen = set([start])
total = 0
for _ in range(3000):
    x, y, z = hq.heappop(frontier)[1]
    for dx, dy, dz in adjacencies:
        next_pos = (x + dx, y + dy, z + dz)
        if next_pos in seen:
            continue
        if next_pos in positions:
            total += 1
            continue
        seen.add(next_pos)
        hq.heappush(frontier, (dist(next_pos, avg), next_pos))

search_xvals, search_yvals, search_zvals = [], [], []
for x, y, z in seen:
    search_xvals.append(x)
    search_yvals.append(y)
    search_zvals.append(z)

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection="3d")
ax.scatter(xvals, yvals, zvals, alpha=0.4)
ax.scatter(search_xvals, search_yvals, search_zvals, c="purple", alpha=0.4, s=10)
ax.scatter(*start, c="red", marker="*")
ax.text(*start, "start")
ax.scatter(*avg, c="green", marker="o", s=400)
ax.text(*avg, "average")
plt.show()
