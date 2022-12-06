# ans = 8109

from collections import Counter

with open("i1.txt") as f:
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
    r = sack[mid:]
    for c in r:
        if c in l:
            total += get_score(c)
            break


print(total)
