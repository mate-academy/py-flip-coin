import random


def flip_coin() -> dict:
    result = []

    for _ in range(10000):
        toss_coin = ""
        for i in range(10):
            toss_coin += str(random.randint(0, 1))

        result.append(toss_coin.count("0"))

    flip_coin_result = {}

    for i in range(11):
        flip_coin_result[i] = round((result.count(i) / 10000) * 100, 2)

    return flip_coin_result
