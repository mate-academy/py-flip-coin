from random import choice


def flip_coin() -> dict:
    exp_count = 10000
    flips = 10
    coin = ["head", "eagle"]
    result = [
        [choice(coin) for i in range(flips)].count("head")
        for _ in range(exp_count)
    ]
    return {
        i: round(result.count(i) / exp_count * 100, 2)
        for i in range(flips + 1)
    }
