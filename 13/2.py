# ans = 20952
import json
from functools import cmp_to_key

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    pairs = f.read().strip().split("\n\n")

decoded = [[[2]], [[6]]]
for pair in pairs:
    x, y = pair.split("\n")
    decoded += [json.loads(x), json.loads(y)]

# negative if pair in right order, positive if wrong order, 0 if equal
def comp_pair(left, right):
    match left, right:
        case int(), int():
            return 0 if left == right else left - right
        case int(), list():
            left = [left]
        case list(), int():
            right = [right]
    if left == [] or right == []:
        return 0 if len(left) == len(right) else len(left) - len(right)

    result = comp_pair(left[0], right[0])
    if result != 0:
        return result

    return comp_pair(left[1:], right[1:])


in_order = sorted(decoded, key=cmp_to_key(comp_pair))

decoder_key = (in_order.index([[2]]) + 1) * (in_order.index([[6]]) + 1)
print(decoder_key)
