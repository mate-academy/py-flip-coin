import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    coin_flip_options = ["heads", "tails"]

    for _ in range(10000):
        flips_result = [random.choice(coin_flip_options) for _ in range(10)]
        number_of_heads = flips_result.count("heads")
        result_dict[number_of_heads] += 1 / 100

    return result_dict
