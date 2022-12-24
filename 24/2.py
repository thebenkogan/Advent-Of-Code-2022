# ans = 4091

from collections import deque, defaultdict

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def wind_to_dir(w):
    match w:
        case ">":
            return (1, 0)
        case "v":
            return (0, 1)
        case "<":
            return (-1, 0)
        case "^":
            return (0, -1)


start = (1, 0)
end = (len(lines[0]) - 2, len(lines) - 1)

winds = defaultdict(list)  # maps wind position to list of directions at position
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if col not in ["#", "."]:
            winds[(j, i)].append(wind_to_dir(col))


def step_winds(winds):
    out = defaultdict(list)
    for (x, y), dirs in winds.items():
        for dx, dy in dirs:
            new_x = x + dx
            new_y = y + dy
            if new_x == 0:
                new_x = len(lines[0]) - 2
            elif new_x == len(lines[0]) - 1:
                new_x = 1
            if new_y == 0:
                new_y = len(lines) - 2
            elif new_y == len(lines) - 1:
                new_y = 1
            out[(new_x, new_y)].append((dx, dy))
    return out


# returns the minimum steps from [start] to [end] with the current [winds]
# configuration; also returns the winds positions after the minimum steps
def get_min_steps(start, end, winds):
    frontier = deque([(start, 0)])
    seen = set([(start, 0)])
    wind_positions = [winds]
    while True:
        pos, steps = frontier.popleft()
        if len(wind_positions) == steps + 1:
            wind_positions.append(step_winds(wind_positions[-1]))
        wind_pos = wind_positions[steps + 1]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_pos = (pos[0] + dx, pos[1] + dy)
            if (next_pos, steps + 1) in seen:
                continue

            if next_pos == end:
                return steps + 1, wind_pos

            nx, ny = next_pos
            if nx == 0 or nx == len(lines[0]) - 1 or ny <= 0 or ny >= len(lines) - 1:
                continue

            if next_pos not in wind_pos:
                seen.add(((next_pos, steps + 1)))
                frontier.append((next_pos, steps + 1))

        # wait if no wind gonna move here next
        if (pos, steps + 1) in seen:
            continue

        if pos not in wind_pos:
            seen.add((pos, steps + 1))
            frontier.append((pos, steps + 1))


first_steps, first_winds = get_min_steps(start, end, winds)
second_steps, second_winds = get_min_steps(end, start, first_winds)
third_steps, _ = get_min_steps(start, end, second_winds)


print(first_steps + second_steps + third_steps)
