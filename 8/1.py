# ans = 1679

with open("i1.txt") as f:
    trees = [line.strip() for line in f.readlines()]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

total = 0
for i, row in enumerate(trees):
    for j, col in enumerate(row):
        curr_height = int(col)
        for dx, dy in directions:
            px, py = j + dx, i + dy
            visible = True
            while 0 <= px < len(row) and 0 <= py < len(trees):
                tree_height = int(trees[py][px])
                if tree_height >= curr_height:
                    visible = False
                    break
                px += dx
                py += dy

            if visible:
                total += 1
                break

print(total)
