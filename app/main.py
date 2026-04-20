import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    result_of_flip = {}

    for _ in range(10000):
        numbers_of_heads = sum(
            random.choice(coin) == "heads"
            for _ in range(10)
        )

        result_of_flip[numbers_of_heads] = result_of_flip.get(
            numbers_of_heads, 0) + 1

    for key, value in result_of_flip.items():
        result_of_flip.update({key: round((value / 10_000) * 100, 2)})
    return dict(sorted(result_of_flip.items()))
