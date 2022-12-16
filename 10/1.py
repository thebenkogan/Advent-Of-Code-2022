# ans = 13760

LAST_CHECKPOINT = 220
CHECKPOINT_STEP = 40

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    instructions = [line.strip() for line in f.readlines()]

total = 0
cycles = 0
next_checkpoint = 20
x = 1


def update(checkpoint):
    global total, next_checkpoint
    total += x * checkpoint
    next_checkpoint += CHECKPOINT_STEP


for i in instructions:
    parts = i.split()
    if parts[0] == "noop":
        cycles += 1
        if cycles == next_checkpoint:
            update(next_checkpoint)
        continue

    val = int(parts[1])
    if cycles + 2 >= next_checkpoint:
        update(next_checkpoint)

    cycles += 2
    x += val

    if next_checkpoint > LAST_CHECKPOINT:
        break


print(total)
