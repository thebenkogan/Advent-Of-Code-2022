# ans = 2493

KNOTS = 10

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    moves = [line.strip() for line in f.readlines()]

dir_map = {"R": (1, 0), "L": (-1, 0), "D": (0, -1), "U": (0, 1)}


visited = set([(0, 0)])
positions = [(0, 0)] * KNOTS
for move in moves:
    dir, steps = move.split()
    dx, dy = dir_map[dir]
    for _ in range(int(steps)):
        positions[0] = positions[0][0] + dx, positions[0][1] + dy
        for i in range(1, KNOTS):
            px, py = positions[i - 1]
            cx, cy = positions[i]
            match (abs(px - cx), abs(py - cy)):
                case (2, _) | (_, 2):
                    next_x = (px + cx) / 2 if abs(px - cx) == 2 else px
                    next_y = (py + cy) / 2 if abs(py - cy) == 2 else py
                    positions[i] = next_x, next_y

        visited.add(positions[-1])


print(len(visited))
