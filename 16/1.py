# ans = 1862

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    valves = [line.strip() for line in f.readlines()]

adj = {}
for valve in valves:
    valve, edges = valve.split(";")
    valve, fr = valve.split("=")
    fr = int(fr)
    valve = valve.split()[1]
    edges = [e[:2] for e in edges.split()[4:]]
    adj[valve] = (fr, edges)


cache = {}


def find_best(node, mins_left, opened):
    key = "".join(opened) + node + str(mins_left)
    if key in cache:
        return cache[key]

    if mins_left <= 0:
        return 0

    fr, edges = adj[node]

    # two options:
    # open curr and move elsewhere with eventual pressure
    # don't open curr and move elsewhere
    # if flow rate is zero or already opened, don't consider opening

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


print(find_best("AA", 30, []))
