# ans = 1644735

from collections import defaultdict

MAX_SIZE = 100_000

with open("i1.txt") as f:
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
        case [size_str, _] if "$" != size_str != "dir":
            for v in dir_path:
                dir_sizes[v] += int(size_str)

total = sum([size for size in dir_sizes.values() if size <= MAX_SIZE])
print(total)
