# ans = 6087

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    moves = [line.strip() for line in f.readlines()]

dir_map = {"R": (1, 0), "L": (-1, 0), "D": (0, -1), "U": (0, 1)}

visited = set([(0, 0)])
head_pos = (0, 0)
tail_pos = (0, 0)
for move in moves:
    dir, steps = move.split()
    dx, dy = dir_map[dir]
    for _ in range(int(steps)):
        head_pos = head_pos[0] + dx, head_pos[1] + dy

        match (abs(head_pos[0] - tail_pos[0]), abs(head_pos[1] - tail_pos[1])):
            case (2, _) | (_, 2):
                # move to previous head location
                tail_pos = head_pos[0] - dx, head_pos[1] - dy
                visited.add(tail_pos)


print(len(visited))
