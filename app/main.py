import random


def flip_coin() -> dict:

    flips_coin = {key: 0 for key in range(11)}
    coin = ["head", "tail"]
    for _ in range(10000):
        count_head = 0

        for _ in range(10):
            if random.choice(coin) == "head":
                count_head += 1

        flips_coin[count_head] += 1

    return {key: (value / 100) for key, value in flips_coin.items()}
