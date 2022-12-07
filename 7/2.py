# ans = 1300850

from collections import defaultdict
import math

DISK_SPACE = 70_000_000
THRESHOLD = 30_000_000

with open("i2.txt") as f:
    commands = f.readlines()

dir_path = []
dir_sizes = defaultdict(int)
for c in commands:
    c = c.split("\n")[0].split(" ")
    match c:
        case ["$", "cd", ".."]:
            dir_path.pop()
        case ["$", "cd", dir]:
            ext = f"/{dir if dir != '/' else ''}"
            dir_path.append("/".join(dir_path) + ext)
        case ["$", "ls"]:
            continue
        case [size_str, _] if size_str != "dir":
            for v in dir_path:
                dir_sizes[v] += int(size_str)

remaining = THRESHOLD - (DISK_SPACE - dir_sizes["/"])
best = math.inf
for size in dir_sizes.values():
    if size >= remaining:
        best = min(size, best)

print(best)
