# ans = 50412

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    lines = [line.strip("\n") for line in f.readlines() if line != "\n"]

map = lines[:-1]
moves_str = lines[-1]
moves = []

i = 0
while i < len(moves_str):
    start = i
    while i < len(moves_str) and moves_str[i] != "R" and moves_str[i] != "L":
        i += 1
    moves.append(int(moves_str[start:i]))
    if i != len(moves_str):
        moves.append(moves_str[i])
    i += 1

row_map = []  # row_map[i] is the start and end x coord of the ith row
col_map = []  # col_map[i] is the start and end y coord of the ith col
max_x = 0
for i in range(len(map)):
    start, end = None, None
    for j in range(len(map[i])):
        max_x = max(max_x, j)
        if map[i][j] != " " and start == None:
            start = j
        elif j == len(map[i]) - 1 or (map[i][j] == " " and start != None):
            end = j - 1 if map[i][j] == " " else j
            break
    row_map.append((start, end))
for i in range(max_x + 1):
    start, end = None, None
    for j in range(len(map)):
        if i < len(map[j]) and map[j][i] != " " and start == None:
            start = j
        if start == None:
            continue
        if i >= len(map[j]) or j == len(map) - 1 or map[j][i] == " ":
            end = j - 1 if i >= len(map[j]) or map[j][i] == " " else j
            break
    col_map.append((start, end))


# [dir] is the current direction, [turn] is one of L or R
def rotate(dir, turn):
    match dir, turn:
        case ((0, 1), "R") | ((0, -1), "L"):
            return (-1, 0)
        case ((0, -1), "R") | ((0, 1), "L"):
            return (1, 0)
        case ((1, 0), "R") | ((-1, 0), "L"):
            return (0, 1)
        case ((-1, 0), "R") | ((1, 0), "L"):
            return (0, -1)


def move(steps, pos, dir):
    x, y = pos
    dx, dy = dir
    for _ in range(steps):
        nx, ny = (x + dx, y + dy)

        if dx != 0:
            if nx < row_map[ny][0]:
                nx = row_map[ny][1]
            elif nx > row_map[ny][1]:
                nx = row_map[ny][0]
        elif dy != 0:
            if ny < col_map[nx][0]:
                ny = col_map[nx][1]
            elif ny > col_map[nx][1]:
                ny = col_map[nx][0]

        if map[ny][nx] == "#":
            break

        x, y = nx, ny

    return x, y


pos = row_map[0][0], 0
dir = (1, 0)
for m in moves:
    match m:
        case int():
            pos = move(m, pos, dir)
        case str():
            dir = rotate(dir, m)


dir_value_map = {
    (1, 0): 0,
    (0, 1): 1,
    (-1, 0): 2,
    (0, -1): 3,
}

print((pos[1] + 1) * 1000 + (pos[0] + 1) * 4 + dir_value_map[dir])
