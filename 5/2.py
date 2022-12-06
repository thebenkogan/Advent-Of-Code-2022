# ans = TZLTLWRNF

stacks = [
    ["M", "F", "C", "W", "T", "D", "L", "B"],
    ["L", "B", "N"],
    ["V", "L", "T", "H", "C", "J"],
    ["W", "J", "P", "S"],
    ["R", "L", "T", "F", "C", "S", "Z"],
    ["Z", "N", "H", "B", "G", "D", "W"],
    ["N", "C", "G", "V", "P", "S", "M", "F"],
    ["Z", "C", "V", "F", "J", "R", "Q", "W"],
    ["H", "L", "M", "P", "R"],
]

with open("i2.txt") as f:
    steps = f.readlines()


for step in steps:
    sp = step.split(" ")
    num = int(sp[1])
    start = int(sp[3]) - 1
    end = int(sp[5]) - 1

    moved = stacks[start][:num]
    stacks[start] = stacks[start][num:]
    stacks[end] = moved + stacks[end]


out = ""
for stack in stacks:
    out += stack[0] if len(stack) > 0 else ""

print(out)
