# ans = 3452

from collections import deque

WINDOW_LENGTH = 14

with open("i2.txt") as f:
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
