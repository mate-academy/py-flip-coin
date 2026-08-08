import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    statistic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        result = 0
        for _ in range(10):
            if random.choice(coin) == "heads":
                result += 1
        statistic[result] += 1

    for key in statistic:
        statistic[key] /= 100

    return statistic
