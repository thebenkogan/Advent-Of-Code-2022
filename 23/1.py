# ans = 4091

from collections import Counter
import math

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    lines = [line.strip() for line in f.readlines()]

ROUNDS = 10

D_MAP = {
    "N": [(0, -1), (-1, -1), (1, -1)],
    "S": [(0, 1), (-1, 1), (1, 1)],
    "W": [(-1, 0), (-1, 1), (-1, -1)],
    "E": [(1, 0), (1, -1), (1, 1)],
}
D = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

elves = set()
for y, line in enumerate(lines):
    for x, tile in enumerate(line):
        if tile == "#":
            elves.add((x, y))


dirs = ["N", "S", "W", "E"]

for i in range(ROUNDS):
    proposals = Counter()
    assignments = {}
    for (x, y) in elves:
        valid = True
        for dx, dy in D:
            if (x + dx, y + dy) in elves:
                valid = False
                break

        if valid:
            continue

        propose_dir = None
        for d in dirs:
            d = D_MAP[d]
            propose = True
            for dx, dy in d:
                if (x + dx, y + dy) in elves:
                    propose = False
                    break
            if propose:
                propose_dir = d[0]
                break

        if propose_dir != None:
            dx, dy = propose_dir
            proposals[(x + dx, y + dy)] += 1
            assignments[(x, y)] = propose_dir

    for elf, propose_dir in assignments.items():
        x, y = elf
        dx, dy = propose_dir
        if proposals[(x + dx, y + dy)] == 1:
            elves.remove(elf)
            elves.add((x + dx, y + dy))

    dirs.append(dirs.pop(0))

min_x, max_x, min_y, max_y = math.inf, -math.inf, math.inf, -math.inf
for x, y in elves:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

total = (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)
print(total)
