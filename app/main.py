import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]

    result = {}

    for _ in range(10000):
        number_of_heads = 0

        for _ in range(10):
            if random.choice(coin) == "heads":
                number_of_heads += 1

        if number_of_heads not in result:
            result[number_of_heads] = 1 / 10000 * 100
        result[number_of_heads] += 1 / 10000 * 100

    return result
