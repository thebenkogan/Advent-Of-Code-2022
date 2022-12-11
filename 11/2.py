# ans = 23641658401

NUM_ROUNDS = 10_000

with open("i2.txt") as f:
    monkeys = f.read().split("\n\n")


class Monkey:
    num_inspected = 0

    def __init__(self, monkey_desc: str):
        lines = [line.strip() for line in monkey_desc.split("\n")]
        self.id = int(lines[0][-2])
        self.items = [int(num) for num in lines[1][16:].split(",")]
        self.op = lines[2].split()[-3:]
        self.test_guard = int(lines[3].split()[-1])
        self.test_true = int(lines[4].split()[-1])
        self.test_false = int(lines[5].split()[-1])

    def throw_next(self, item, monkeys: list["Monkey"], lcm):
        self.num_inspected += 1
        match self.op:
            case ["old", "*", num]:
                num = item if num == "old" else int(num)
                item *= num
            case ["old", "+", num]:
                num = item if num == "old" else int(num)
                item += num
        item %= lcm
        throw_index = self.test_true if item % self.test_guard == 0 else self.test_false
        monkeys[throw_index].items.append(item)

    def take_turn(self, monkeys: list["Monkey"], lcm):
        for item in self.items:
            self.throw_next(item, monkeys, lcm)
        self.items = []


monkeys = [Monkey(desc) for desc in monkeys]
lcm = 1
for monkey in monkeys:
    lcm *= monkey.test_guard

for i in range(NUM_ROUNDS):
    for monkey in monkeys:
        monkey.take_turn(monkeys, lcm)

monkeys = sorted(monkeys, key=lambda m: m.num_inspected, reverse=True)
print(monkeys[0].num_inspected * monkeys[1].num_inspected)
