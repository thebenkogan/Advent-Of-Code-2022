# ans = 1036

from collections import Counter

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    lines = [line.strip() for line in f.readlines()]

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

all_valid = False
num_rounds = 0
proposals = Counter()
assignments = {}
while not all_valid:
    num_rounds += 1
    round_good = True
    for (x, y) in elves:
        valid = True
        for dx, dy in D:
            if (x + dx, y + dy) in elves:
                valid = False
                break

        if valid:
            continue

        round_good = False
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
    assignments.clear()
    proposals.clear()

    all_valid = round_good

print(num_rounds)
