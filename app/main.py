import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    result = {}
    for _ in range(10000):
        num_of_heads = sum(random.choice(coin) == "heads"
                           for _ in range(10))

        result[num_of_heads] = result.get(num_of_heads, 0) + 1

    for key, value in result.items():
        result[key] = round((value / 10_000) * 100, 2)
    return dict(sorted((result.items())))
