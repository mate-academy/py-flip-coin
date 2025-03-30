import random


def flip_coin() -> None:
    coin = ["heads", "tails"]
    result = {key: 0 for key in range(11)}

    for _ in range(10_000):
        heads_count = 0
        for _ in range(10):
            side_of_coin = random.choice(coin)
            if side_of_coin == "heads":
                heads_count += 1
        result[heads_count] += 1

    for index in range(11):
        result[index] = round((result[index] * 100) / 10_000, 2)
    return result
