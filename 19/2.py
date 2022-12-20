# ans = 2700

from collections import deque

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    blueprint_descs = [line.strip() for line in f.readlines()]

MINUTES = 32


class Blueprint:
    def __init__(self, id, ore_cost, clay_cost, obsidian_cost, geode_cost):
        self.id = id
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost
        self.geode_cost = geode_cost
        self.max_ore_cost = max([ore_cost, clay_cost, obsidian_cost[0], geode_cost[0]])


blueprints = []
for blueprint in blueprint_descs[:3]:
    id, costs = blueprint.split(":")
    id = int(id.split()[-1])
    costs = costs.split()
    ore_cost = int(costs[4])
    clay_cost = int(costs[10])
    obsidian_cost = (int(costs[16]), int(costs[19]))
    geode_cost = (int(costs[25]), int(costs[28]))
    blueprints.append(Blueprint(id, ore_cost, clay_cost, obsidian_cost, geode_cost))


class State:
    def __init__(self, t, o, c, ob, g, o_rate, c_rate, ob_rate, g_rate):
        self.mins_left = t
        self.num_ore = o
        self.num_clay = c
        self.num_obsidian = ob
        self.num_geode = g
        self.ore_rate = o_rate
        self.clay_rate = c_rate
        self.obsidian_rate = ob_rate
        self.geode_rate = g_rate

    def step(self, bp: Blueprint):
        self.num_ore += self.ore_rate
        self.num_clay += self.clay_rate
        self.num_obsidian += self.obsidian_rate
        self.num_geode += self.geode_rate
        self.mins_left -= 1

        # clear excess
        ore_gain = self.ore_rate * (self.mins_left - 1)
        clay_gain = self.clay_rate * (self.mins_left - 1)
        obsidian_gain = self.obsidian_rate * (self.mins_left - 1)
        ore_max = self.mins_left * bp.max_ore_cost
        clay_max = self.mins_left * bp.obsidian_cost[1]
        obsidian_max = self.mins_left * bp.geode_cost[1]
        if self.num_ore >= ore_max - ore_gain:
            self.num_ore = ore_max - ore_gain
        if self.num_clay >= clay_max - clay_gain:
            self.num_clay = clay_max - clay_gain
        if self.num_obsidian >= obsidian_max - obsidian_gain:
            self.num_obsidian = obsidian_max - obsidian_gain

    def neighbors(self, bp: Blueprint, seen):
        tp = self.tuple()
        t, o, c, ob, g, o_r, c_r, ob_r, g_r = tp
        ooc, occ = bp.obsidian_cost
        goc, gobc = bp.geode_cost

        # just build a geode robot if we can
        if o >= goc and ob >= gobc:
            s = State(t, o - goc, c, ob - gobc, g - 1, o_r, c_r, ob_r, g_r + 1)
            s.step(bp)
            return [s] if s not in seen else []

        neighbors = []
        if o >= bp.ore_cost and o_r < bp.max_ore_cost:
            s = State(t, o - bp.ore_cost - 1, c, ob, g, o_r + 1, c_r, ob_r, g_r)
            neighbors.append(s)
        if o >= bp.clay_cost and c_r < occ:
            s = State(t, o - bp.clay_cost, c - 1, ob, g, o_r, c_r + 1, ob_r, g_r)
            neighbors.append(s)
        if o >= ooc and c >= occ and ob_r < bp.geode_cost[1]:
            s = State(t, o - ooc, c - occ, ob - 1, g, o_r, c_r, ob_r + 1, g_r)
            neighbors.append(s)
        # don't build nothing if we can build everything
        if len(neighbors) < 3:
            s = State(t, o, c, ob, g, o_r, c_r, ob_r, g_r)
            neighbors.append(s)

        filtered_neighbors = []
        for n in neighbors:
            n.step(bp)
            if n not in seen:
                filtered_neighbors.append(n)

        return filtered_neighbors

    def tuple(self):
        return (
            self.mins_left,
            self.num_ore,
            self.num_clay,
            self.num_obsidian,
            self.num_geode,
            self.ore_rate,
            self.clay_rate,
            self.obsidian_rate,
            self.geode_rate,
        )

    # does not include the minutes left in the hash/eq, rationale:
    # if we have already seen the same state with only a time difference,
    # then the one with more minutes left is preferable since it will
    # have the opportunity to build more things

    def __hash__(self):
        return hash(self.tuple()[1:])

    def __eq__(self, o):
        return self.tuple()[1:] == o.tuple()[1:]


def get_blueprint_score(bp: Blueprint):
    start = State(MINUTES, 0, 0, 0, 0, 1, 0, 0, 0)
    frontier = deque([start])
    seen = set([start])
    max_geodes = (0, 0)  # (best # of geodes, time found)

    while len(frontier) > 0:
        s = frontier.popleft()

        # skip if less geodes than current best and not enough time to catch up
        if s.num_geode < max_geodes[0] and s.mins_left < max_geodes[1]:
            continue

        if s.num_geode > max_geodes[0]:
            max_geodes = s.num_geode, s.mins_left

        if s.mins_left == 0:
            continue

        neighbors = s.neighbors(bp, seen)
        seen.update(neighbors)
        frontier.extend(neighbors)

    print(max_geodes[0])
    return max_geodes[0]


ans = 1
for blueprint in blueprints:
    ans *= get_blueprint_score(blueprint)

print(ans)
