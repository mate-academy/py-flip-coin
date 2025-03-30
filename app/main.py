import random


def flip_coin(
        num_flips: int = 10000, num_coin_tosses: int = 10
) -> dict:
    results = {i: 0 for i in range(num_coin_tosses + 1)}

    for _ in range(num_flips):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_coin_tosses))
        results[num_heads] += 1

    percentages = (
        {key: (value / num_flips) * 100 for key, value in results.items()}
    )
    return percentages
