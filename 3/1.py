# ans = 8109

from collections import Counter

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    sacks = f.readlines()


def get_score(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38


total = 0
for sack in sacks:
    mid = int(len(sack) / 2)
    l = set(sack[:mid])
    r = set(sack[mid:])
    ans = l.intersection(r).pop()
    total += get_score(ans)

print(total)
