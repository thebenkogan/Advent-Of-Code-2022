# ans = 5112034

# algorithm:
# for each sensor, beacon pair:
# find all x positions in target row that cannot be a beacon

# put it mathematically:
#
# let s = sensor position, b = beacon position, c = candidate position
# manhattan distance to candidate should be less than or equal to distance to beacon
#
# dist(s, c) = abs(cx - sx) + abs(cy - sy) <= dist(s, b)
#
# cy is given, solve for cx:
#
# let r = abs(cy - sy)
# let d = dist(s, b)
# abs(cx - sx) + r <= d
# abs(cx - sx) <= d - r [no solution if d - r < 0]
# r - d <= cx - sx <= d - r
# r - d + sx <= cx <= d - r + sx

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    positions = [line.strip() for line in f.readlines()]

ROW = 10 if test else 2_000_000


def get_coords(s):
    x, y = s.split()[-2:]
    return (int(x[2:-1]), int(y[2:]))


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


non_beacons_x = set()
for sensor in positions:
    s, b = sensor.split(":")
    sx, sy = get_coords(s)
    bx, by = get_coords(b)
    r = abs(sy - ROW)
    d = dist((sx, sy), (bx, by))
    xs = range(r - d + sx, d - r + sx + 1)
    if d - r >= 0:
        non_beacons_x = non_beacons_x.union(xs)
    if by == ROW and bx in non_beacons_x:
        non_beacons_x.remove(bx)

print(len(non_beacons_x))
