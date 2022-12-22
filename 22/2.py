# ans = 130068

with open("in.txt") as f:
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

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

R = len(map)
C = len(map[0])
for r in range(R):
    while len(map[r]) < C:
        map[r] += " "
    assert len(map[r]) == C


CUBE = 50
REGION = [(0, 1), (0, 2), (1, 1), (2, 1), (2, 0), (3, 0)]


def regionToGlobal(r, c, region):
    rr, cc = REGION[region - 1]
    return (rr * CUBE + r, cc * CUBE + c)


def getRegion(r, c):
    for i, (rr, cc) in enumerate(REGION):
        if rr * CUBE <= r < (rr + 1) * CUBE and cc * CUBE <= c < (cc + 1) * CUBE:
            return (i + 1, r - rr * CUBE, c - cc * CUBE)
    assert False, (r, c)


def newCoords(r, c, d, nd):
    if d == 0:
        assert r == 0
        x = c
    if d == 1:
        assert c == CUBE - 1
        x = r
    if d == 2:
        assert r == CUBE - 1
        x = CUBE - 1 - c
    if d == 3:
        assert c == 0
        x = CUBE - 1 - r

    if nd == 0:
        return (CUBE - 1, x)
    if nd == 1:
        return (x, 0)
    if nd == 2:
        return (0, CUBE - 1 - x)
    if nd == 3:
        return (CUBE - 1 - x, CUBE - 1)


def getDest(r, c, d):
    region, rr, rc = getRegion(r, c)
    # 0=up, 1=right,2=down,3=left
    # If I am leaving region R in direction D, I enter region NR in direction ND
    newRegion, nd = {
        (4, 0): (3, 0),
        (4, 1): (2, 3),
        (4, 2): (6, 3),
        (4, 3): (5, 3),
        (1, 0): (6, 1),
        (1, 1): (2, 1),
        (1, 2): (3, 2),
        (1, 3): (5, 1),
        (3, 0): (1, 0),
        (3, 1): (2, 0),
        (3, 2): (4, 2),
        (3, 3): (5, 2),
        (6, 0): (5, 0),
        (6, 1): (4, 0),
        (6, 2): (2, 2),
        (6, 3): (1, 2),
        (2, 0): (6, 0),
        (2, 1): (4, 3),
        (2, 2): (3, 3),
        (2, 3): (1, 3),
        (5, 0): (3, 1),
        (5, 1): (4, 1),
        (5, 2): (6, 2),
        (5, 3): (1, 1),
    }[(region, d)]

    nr, nc = newCoords(rr, rc, d, nd)
    assert 0 <= nr < CUBE and 0 <= nc < CUBE
    nr, nc = regionToGlobal(nr, nc, newRegion)
    assert map[nr][nc] in [".", "#"], f"{map[nr][nc]}"
    return (nr, nc, nd)


def rotate(dir, turn):
    if turn == "L":
        dir = (dir + 3) % 4
    elif turn == "R":
        dir = (dir + 1) % 4
    return dir


def move(n, pos, dir):
    r, c = pos
    for _ in range(n):
        rr = (r + D[dir][0]) % R
        cc = (c + D[dir][1]) % C
        if map[rr][cc] == " ":
            (nr, nc, nd) = getDest(r, c, dir)
            if map[nr][nc] == "#":
                break
            (r, c, dir) = (nr, nc, nd)
            continue
        elif map[rr][cc] == "#":
            break
        else:
            r = rr
            c = cc

    return (r, c), dir


pos = 0, row_map[0][0]
dir = 1
for m in moves:
    match m:
        case int():
            pos, dir = move(m, pos, dir)
        case str():
            dir = rotate(dir, m)


DV = {0: 3, 1: 0, 2: 1, 3: 2}
print((pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + DV[dir])
