# ans = 20=2-02-0---02=22=21

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    lines = [line.strip() for line in f.readlines()]

SNAFU_VAL = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


def snafu_to_decimal(s):
    out = 0
    for i, c in enumerate(s):
        out += (5 ** (len(s) - i - 1)) * SNAFU_VAL[c]
    return out


def dec_to_snafu(n):
    out = ""
    while n > 0:
        match n % 5:
            case n if n <= 2:
                out = str(n) + out
                n //= 5
            case 3:
                out = "-" + out
                n = (n + 1) // 5
            case 4:
                out = "=" + out
                n = (n + 2) // 5
    return int(out)


total = sum([snafu_to_decimal(line) for line in lines])
print(dec_to_snafu(total))
