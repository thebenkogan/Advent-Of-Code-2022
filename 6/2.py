# ans = 3452

from collections import deque

WINDOW_LENGTH = 14

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    signal = f.read()

start = 0
window = deque([])
for i, c in enumerate(signal):
    if i < WINDOW_LENGTH:
        window.append(c)
        continue

    if len(set(window)) == len(window):
        start = i
        break

    window.append(c)
    window.popleft()


print(start)
