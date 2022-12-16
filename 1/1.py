# ans = 68467

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
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
