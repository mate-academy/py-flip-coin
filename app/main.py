# write your code here
# heads - орел
# tails - решка
import random


def flip_coin() -> dict:
    sides_of_coin = ["heads", "tails"]
    all_tests = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    first_count = 0
    while first_count < 10000:
        first_count += 1

        heads = 0
        second_count = 0
        while second_count < 10:
            second_count += 1
            if random.choice(sides_of_coin) == "heads":
                heads += 1

        all_tests[heads] += 1

    for key in all_tests:
        all_tests[key] = round(all_tests[key] / 10000 * 100, 2)

    return all_tests
