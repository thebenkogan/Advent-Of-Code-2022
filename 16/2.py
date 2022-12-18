# ans = 2422

# algorithm:
# generate all splits of non-zero flow rate valves
# do 1 run with one of the partitions as already opened
# do another run with the other partition already opened

# this is horribly inefficient, the better way is with recursion:
# once you run out of time on the first run, make a new recursive call and
# reset with 26 mins, persisting the opened valves
# can't get around max recursion depth issues though :(

from itertools import combinations, chain

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    valves = [line.strip() for line in f.readlines()]

adj = {}
nonzero_valves = []
for valve in valves:
    valve, edges = valve.split(";")
    valve, fr = valve.split("=")
    fr = int(fr)
    valve = valve.split()[1]
    edges = [e[:2] for e in edges.split()[4:]]
    adj[valve] = (fr, edges)
    if fr > 0:
        nonzero_valves.append(valve)


cache = {}


def find_best(node, mins_left, opened):
    key = "".join(opened) + node + str(mins_left)
    if key in cache:
        return cache[key]

    if mins_left <= 0:
        return 0

    fr, edges = adj[node]

    best = 0
    ep = fr * (mins_left - 1)
    should_open = fr > 0 and node not in opened
    open_arr = sorted([*opened, node]) if should_open else opened
    for edge in edges:
        # open
        if should_open:
            best = max(best, ep + find_best(edge, mins_left - 2, open_arr))

        # don't open
        best = max(best, find_best(edge, mins_left - 1, opened))

    cache[key] = best
    return best


subsets = [
    v for a in range(len(nonzero_valves)) for v in combinations(nonzero_valves, a)
]
combos = []
for i in range(len(subsets) // 2 + 1):
    combos.append(
        (list(chain(subsets[i])), [e for e in nonzero_valves if e not in subsets[i]])
    )

best = 0
for us, el in combos:
    best = max(best, find_best("AA", 26, us) + find_best("AA", 26, el))

print(best)
