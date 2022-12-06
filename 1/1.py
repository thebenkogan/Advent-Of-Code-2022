# ans = 68467

with open("i1.txt") as f:
    calories = f.readlines()

max_elf = 0
count = 0
for cal in calories:
    if cal == "\n":
        max_elf = max(count, max_elf)
        count = 0
    else:
        count += int(cal)

print(max_elf)
