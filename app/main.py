import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        num_heads = sum(random.randint(0, 1) for _ in range(10))
        results[num_heads] += 1

    return {key: (value / 10000 * 100) for key, value in results.items()}
