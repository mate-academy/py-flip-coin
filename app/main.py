import random


def flip_coin() -> dict:
    coin = ["head", "bottom"]
    cases = {i: 0 for i in range(11)}
    for _ in range(10000):
        count_head = 0
        for __ in range(10):
            side_of_coin = random.choice(coin)
            if side_of_coin == "head":
                count_head += 1
        cases[count_head] += 1
    cases_percentage = {}
    for case in cases:
        cases_percentage[case] = cases[case] / 100
    return cases_percentage
