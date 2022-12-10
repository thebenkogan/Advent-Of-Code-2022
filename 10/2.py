# ans = RFKZCPEF

CRT_HEIGHT = 6
CRT_WIDTH = 40

with open("i2.txt") as f:
    instructions = [line.strip() for line in f.readlines()]

x = 1
CRT_out = [[] for _ in range(CRT_HEIGHT)]
CRT_row = 0


def write_CRT():
    global CRT_out, CRT_row, x
    pixel = "#" if len(CRT_out[CRT_row]) in range(x - 1, x + 2) else "."
    CRT_out[CRT_row] += pixel
    CRT_row += 1 if len(CRT_out[CRT_row]) == CRT_WIDTH else 0


for i in instructions:
    write_CRT()

    parts = i.split()
    if parts[0] == "noop":
        continue

    write_CRT()

    val = int(parts[1])
    x += val

print("\n".join(["".join(row) for row in CRT_out]))
