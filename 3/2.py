# ans = 2738

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
for i in range(0, len(sacks), 3):
    l = set(sacks[i].strip())
    m = set(sacks[i + 1].strip())
    r = set(sacks[i + 2].strip())
    ans = l.intersection(m).intersection(r)
    total += get_score(ans.pop())


print(total)
