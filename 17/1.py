# ans = 3186

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    jet = f.read().strip()

PIECES = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (1, 1), (0, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]

WIDTH = 7

NUM_ROCKS = 2022


def piece_generator():
    i = 0
    count = 0
    while count < NUM_ROCKS:
        yield PIECES[i]
        i += 1
        count += 1
        if i == len(PIECES):
            i = 0


pgen = piece_generator()


def move_generator():
    dir_map = {"<": (-1, 0), ">": (1, 0)}
    moves = []
    for j in jet:
        moves.append(dir_map[j])
        moves.append((0, -1))
    i = 0
    while True:
        yield moves[i]
        i += 1
        if i == len(moves):
            i = 0


mgen = move_generator()


class Piece:
    def __init__(self, layout, pos):
        x, y = pos
        self.blocks = [(lx + x, ly + y) for (lx, ly) in layout]

    # moves in [dir] direction with the current set of [stopped_rocks]. Returns
    # True if rock stopped (impossible downward movement)
    def move(self, dir, stopped_rocks):
        dx, dy = dir
        temp_blocks = [(px + dx, py + dy) for (px, py) in self.blocks]
        valid = True
        for (tx, ty) in temp_blocks:
            if tx < 0 or tx >= WIDTH or ty < 0 or (tx, ty) in stopped_rocks:
                valid = False
                break

        if valid:
            self.blocks = temp_blocks

        return valid or dir != (0, -1)

    # dumps the current piece positions into [stopped_rocks]
    # returns the new highest block height
    def dump(self, stopped_rocks, highest_rock):
        for piece in self.blocks:
            highest_rock = max(highest_rock, piece[1])
            stopped_rocks.add(piece)
        return highest_rock


highest_rock = -1
stopped_rocks = set()
for piece in pgen:
    pos = (2, highest_rock + 4)
    piece = Piece(piece, pos)
    while piece.move(next(mgen), stopped_rocks):
        pass
    highest_rock = piece.dump(stopped_rocks, highest_rock)


print(highest_rock + 1)
