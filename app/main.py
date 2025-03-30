import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    result_dict = {}

    for _ in range(10_000):

        numbers_of_heads = sum(
            random.choice(coin) == "heads"
            for _ in range(10)
        )

        result_dict[numbers_of_heads] = result_dict.get(
            numbers_of_heads, 0) + 1

    for key, value in result_dict.items():
        result_dict.update({key: round((value / 10_000) * 100, 2)})

    return dict(sorted(result_dict.items()))
