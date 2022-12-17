# ans = 13172087230812

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    positions = [line.strip() for line in f.readlines()]

MAX_COORD = 20 if test else 4_000_000


def get_coords(s):
    x, y = s.split()[-2:]
    return (int(x[2:-1]), int(y[2:]))


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


nodes = []
for sensor in positions:
    s, b = sensor.split(":")
    nodes.append((get_coords(s), get_coords(b)))


def is_beacon(pos):
    for s, b in nodes:
        if dist(s, pos) <= dist(s, b):
            return False
    return True


for s, b in nodes:
    d = dist(s, b) + 1
    sx, sy = s[0], s[1] - d
    for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
        for _ in range(d):
            sx += dx
            sy += dy
            if 0 <= sx < MAX_COORD and 0 <= sy < MAX_COORD and is_beacon((sx, sy)):
                raise Exception(f"{sx * MAX_COORD + sy}")
