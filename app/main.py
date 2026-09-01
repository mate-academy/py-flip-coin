import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    result = {}

    for _ in range(10000):
        count = 0
        for _ in range(0, 10):
            if random.choice(coin) == "heads":
                count += 1
        result[count] = result.get(count, 0) + 1

    for key, value in result.items():
        result[key] = value / 100

    return dict(sorted(result.items()))
