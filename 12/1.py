# ans = 437

from collections import defaultdict, deque

with open("i1.txt") as f:
    rows = [line.strip() for line in f.readlines()]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# maps (x, y) coordinate to list of edge coordinates
adj_map = defaultdict(list)


def get_elevation(height):
    return "a" if height == "S" else "z" if height == "E" else height


for i, row in enumerate(rows):
    for j, col in enumerate(row):
        if col == "S":
            start_coord = (i, j)
        elif col == "E":
            end_coord = (i, j)
        elevation = get_elevation(col)
        for dx, dy in directions:
            px, py = j + dx, i + dy
            if 0 <= px < len(rows[0]) and 0 <= py < len(rows):
                next_elevation = get_elevation(rows[py][px])
                if ord(next_elevation) - ord(elevation) <= 1:
                    adj_map[(i, j)].append((py, px))

best_steps = 0
frontier = deque([(start_coord, 0)])
seen = set()
while len(frontier) > 0:
    coord, steps = frontier.popleft()
    if coord in seen:
        continue
    if coord == end_coord:
        best_steps = steps
        break
    seen.add(coord)
    edges = adj_map[coord]
    for node in edges:
        frontier.append((node, steps + 1))


print(best_steps)
