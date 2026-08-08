import random


def flip_coin(num_flips: int = 10000, num_coins: int = 10) -> dict:
    results = {i: 0 for i in range(num_coins + 1)}

    for _ in range(num_flips):
        num_heads = sum(random.randint(0, 1) for _ in range(num_coins))
        results[num_heads] += 1

    for key, value in results.items():
        results[key] = (value / num_flips) * 100

    return results
