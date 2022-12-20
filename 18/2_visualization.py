# ans = 2520

import heapq as hq
from math import hypot
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

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
xvals, yvals, zvals = (
    np.zeros(len(positions)),
    np.zeros(len(positions)),
    np.zeros(len(positions)),
)
for i, (x, y, z) in enumerate(positions):
    x = max(max_x, x)
    xvals[i] = x
    yvals[i] = y
    zvals[i] = z
    sum_x += x
    sum_y += y
    sum_z += z
avg = (sum_x / len(positions), sum_y / len(positions), sum_z / len(positions))
start = (max_x + 2, 0, 0)

frontier = [(dist(start, avg), start)]
seen = set([start])
total = 0
search_xvals, search_yvals, search_zvals = (
    np.zeros(3000),
    np.zeros(3000),
    np.zeros(3000),
)
for i in range(3000):
    x, y, z = hq.heappop(frontier)[1]
    search_xvals[i] = x
    search_yvals[i] = y
    search_zvals[i] = z
    for dx, dy, dz in adjacencies:
        next_pos = (x + dx, y + dy, z + dz)
        if next_pos in seen:
            continue
        if next_pos in positions:
            total += 1
            continue
        seen.add(next_pos)
        hq.heappush(frontier, (dist(next_pos, avg), next_pos))


fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection="3d")
ax.scatter(xvals, yvals, zvals, s=20, alpha=0.4)
search = ax.scatter([], [], [], c="purple", s=40)


SEARCH_SPEED = 10


def update(i):
    search._offsets3d = (
        search_xvals[: i * SEARCH_SPEED],
        search_yvals[: i * SEARCH_SPEED],
        search_zvals[: i * SEARCH_SPEED],
    )


anim = FuncAnimation(
    fig, update, frames=len(search_xvals) // SEARCH_SPEED, interval=1, repeat=False
)
anim.save("flood.gif", fps=30)
ax.scatter(*start, c="red", marker="*")
ax.text(*start, "start")
ax.scatter(*avg, c="green", marker="o", s=400)
ax.text(*avg, "average")
plt.show()
