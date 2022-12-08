# ans = 536625

with open("i2.txt") as f:
    trees = [line.strip() for line in f.readlines()]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

best = 0
for i, row in enumerate(trees):
    for j, col in enumerate(row):
        curr_height = int(col)
        scenic_score = 1
        for dx, dy in directions:
            px, py = j + dx, i + dy
            num_trees_visible = 0
            while 0 <= px < len(row) and 0 <= py < len(trees):
                tree_height = int(trees[py][px])
                if tree_height >= curr_height:
                    num_trees_visible += tree_height == curr_height
                    break
                num_trees_visible += 1
                px += dx
                py += dy

            scenic_score *= num_trees_visible

        best = max(best, scenic_score)

print(best)
