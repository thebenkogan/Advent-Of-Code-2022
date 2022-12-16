# ans = 5503
import json

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    pairs = f.read().strip().split("\n\n")

decoded = []
for pair in pairs:
    x, y = pair.split("\n")
    decoded.append((json.loads(x), json.loads(y)))

# True if the pair is in the right order, None if order unknown
def comp_pair(left, right):
    match left, right:
        case int(), int():
            return None if left == right else left < right
        case int(), list():
            left = [left]
        case list(), int():
            right = [right]
    if left == [] or right == []:
        return None if len(left) == len(right) else len(left) < len(right)

    result = comp_pair(left[0], right[0])
    if result != None:
        return result

    return comp_pair(left[1:], right[1:])


total = 0
for i, (left, right) in enumerate(decoded):
    if comp_pair(left, right):
        total += i + 1

print(total)
