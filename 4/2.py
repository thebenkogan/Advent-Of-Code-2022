# ans = 835

with open("i2.txt") as f:
    pairs = f.readlines()


def create_range(range_str):
    sp = range_str.split("-")
    return (int(sp[0]), int(sp[1]))


total = 0
for pair in pairs:
    sp = pair.split(",")
    l_min, l_max = create_range(sp[0])
    r_min, r_max = create_range(sp[1])

    if l_min <= r_min <= l_max or r_min <= l_min <= r_max:
        total += 1

print(total)
