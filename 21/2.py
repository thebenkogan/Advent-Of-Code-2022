# ans = 3441198826073

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
    if id == "humn":
        raise Exception

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


# returns the expression represented by id with the identifier to solve for
def get_expr(id):
    a, op, b = env[id]
    try:
        a = eval_id(a)
        var = b
    except:
        pass
    try:
        b = eval_id(b)
        var = a
    except:
        pass

    return ([a, op, b], var)


# exp is an expression with some concrete value and an identifier
# returns the value of the identifier such that [id op val = eq]
def solve_equation(exp, eq):
    match exp:
        case [str(), "+", x] | [x, "+", str()]:
            return eq - x
        case [str(), "-", x]:
            return eq + x
        case [x, "-", str()]:
            return x - eq
        case [str(), "*", x] | [x, "*", str()]:
            return eq / x
        case [str(), "/", x]:
            return eq * x
        case [x, "/", str()]:
            return x / eq


equality, solving_for = get_expr("root")
eq = equality[0] if equality[0] != solving_for else equality[2]
exp, solving_for = get_expr(solving_for)
while True:
    eq = solve_equation(exp, eq)
    if solving_for == "humn":
        print(eq)
        break
    exp, solving_for = get_expr(solving_for)
