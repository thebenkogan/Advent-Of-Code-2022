# ans = 276156919469632

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    expressions = [line.strip() for line in f.readlines()]


env = {}
for exp in expressions:
    id, exp = exp.split(": ")
    exp = exp.split()
    if len(exp) == 1:
        exp = int(exp[0])
    env[id] = exp


def eval_id(id):
    global env

    match env[id]:
        case [a, "+", b]:
            res = eval_id(a) + eval_id(b)
        case [a, "-", b]:
            res = eval_id(a) - eval_id(b)
        case [a, "*", b]:
            res = eval_id(a) * eval_id(b)
        case [a, "/", b]:
            res = eval_id(a) / eval_id(b)
        case n:
            res = n

    env[id] = res
    return res


print(eval_id("root"))
