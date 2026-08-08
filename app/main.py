import random


def flip_coin() -> dict:
    results = {amount: 0 for amount in range(11)}
    coin = ["head", "tail"]

    for i in range(10000):
        head = 0
        for _ in range(10):
            result = random.choice(coin)
            if result == "head":
                head += 1
        results[head] += 1

    statistic = {amount: round((results[amount] / 10000) * 100, 2)
                 for amount in results}

    return statistic
