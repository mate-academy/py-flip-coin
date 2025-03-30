import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    coin = ["heads", "tails"]

    for _ in range(10000):
        count_of_heads = sum(
            1
            for _ in range(10)
            if random.choice(coin) == "heads"
        )
        result_dict[count_of_heads] += 1

    result_dict = {
        key: round((value / 10000) * 100, 2)
        for key, value in result_dict.items()
    }

    return result_dict
