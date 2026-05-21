import random


def flip_coin(fleep_cases: int = 10000) -> dict:
    count = {}
    coin = [0, 1]

    for i in range(11):
        count[i] = 0

    for cases in range(fleep_cases):
        cases_count = 0
        for index in range(10):
            if random.choice(coin) == 1:
                cases_count += 1
        count[cases_count] += 1

    for key, value in count.items():
        count[key] = round(value / fleep_cases * 100, 2)
    return count
