# ans = 2520

# algorithm:
# start at point outside of droplet
# heuristic search to positions closest to the average position in the droplet
# each time we are adjacent to a droplet position, add 1

# we heuristic search so we focus the search space on the outside of the droplet
# need to increase iterations to 3000 to cover whole exterior

import heapq as hq
from math import hypot

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
for x, y, z in positions:
    x = max(max_x, x)
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


print(total)
