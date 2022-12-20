# ans = 1338310513297

import numpy as np

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    numbers = [line.strip() for line in f.readlines()]

DECRYPTION_KEY = 811589153
NUM_MIXES = 10

numbers = np.array([int(n) for n in numbers], dtype="int64")
numbers *= DECRYPTION_KEY

# maps index in moving list to index in original list
d = np.arange(len(numbers))

for _ in range(NUM_MIXES):
    for i in range(len(numbers)):
        index = np.where(d == i)[0][0]
        val = numbers[d[index]]
        target_index = (index + val) % (len(numbers) - 1)
        if target_index == 0 and val < 0:
            target_index = len(numbers) - 1
        if target_index > index:
            d[index:target_index] = d[index + 1 : target_index + 1]
        elif target_index < index:
            d[target_index + 1 : index + 1] = d[target_index:index]
        d[target_index] = i


mixed = numbers[d]
zero_index = np.where(mixed == 0)[0][0]
thousand = mixed[(1000 + zero_index) % len(mixed)]
two_thousand = mixed[(2000 + zero_index) % len(mixed)]
three_thousand = mixed[(3000 + zero_index) % len(mixed)]
print(thousand + two_thousand + three_thousand)
