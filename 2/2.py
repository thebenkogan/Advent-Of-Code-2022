# ans = 10238

test = False

input_name = "test" if test else "in"
with open(f"{input_name}.txt") as f:
    rounds = f.readlines()

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def get_round_result_score(opp, us):
    match (us, opp):
        case ("X", "A") | ("Y", "B") | ("Z", "C"):
            return 3
        case ("X", "C") | ("Y", "A") | ("Z", "B"):
            return 6
    return 0


def get_hand(opp, res):
    match (opp, res):
        case ("B", "X") | ("A", "Y") | ("C", "Z"):
            return "X"
        case ("C", "X") | ("B", "Y") | ("A", "Z"):
            return "Y"
    return "Z"


total = 0
for round in rounds:
    opp = round[0]
    us = get_hand(opp, round[2])
    total += scores[us] + get_round_result_score(opp, us)

print(total)
