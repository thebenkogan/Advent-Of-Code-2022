# ans = 897

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    paths = [line.strip() for line in f.readlines()]


def normalize(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def path_to_joints(path):
    joints = path.split(" -> ")
    joints = list(map(lambda j: j.split(","), joints))
    return list(map(lambda j: (int(j[0]), int(j[1])), joints))


left_width = 0
right_width = 0
max_height = 0
for path in paths:
    for (w, h) in path_to_joints(path):
        right_width = max(w - 500, right_width)
        left_width = max(500 - w, left_width)
        max_height = max(h, max_height)

cave = [["."] * (left_width + right_width + 1) for _ in range(max_height + 1)]
source = left_width, 0

for path in paths:
    joints = path_to_joints(path)
    sx, sy = joints[0]
    for x, y in joints[1:]:
        dx, dy = normalize(x - sx), normalize(y - sy)
        while (sx, sy) != (x + dx, y + dy):
            w = left_width - (500 - sx)
            cave[sy][w] = "#"
            sx += dx
            sy += dy
        sx, sy = x, y

total = 0
done = False
while not done:
    sx, sy = source
    while True:
        sy += 1
        if sy >= len(cave):
            done = True
            break
        if cave[sy][sx] in ["#", "o"]:
            if sx - 1 < 0:
                done = True
                break
            elif cave[sy][sx - 1] not in ["#", "o"]:
                sx -= 1
                continue
            if sx + 1 >= len(cave[0]):
                done = True
                break
            elif cave[sy][sx + 1] not in ["#", "o"]:
                sx += 1
                continue

            total += 1
            cave[sy - 1][sx] = "o"
            break

print("\n".join([" ".join(line) for line in cave]))
print(total)
