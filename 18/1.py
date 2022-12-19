# ans = 4192

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    cubes = [line.strip() for line in f.readlines()]

adjacencies = [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]

positions = set()
for cube in cubes:
    positions.add(tuple([int(n) for n in cube.split(",")]))

total = 0

for x, y, z in positions:
    exposed = 6
    for dx, dy, dz in adjacencies:
        if (x + dx, y + dy, z + dz) in positions:
            exposed -= 1
    total += exposed

print(total)
