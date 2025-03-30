import random


def flip_coin(tries: int = 10000, coin_flips: int = 10) -> dict:
    results = {}
    for _ in range(tries):
        num_heads = sum(random.randint(0, 1) for _ in range(coin_flips))
        results[num_heads] = results.get(num_heads, 0) + 1
    probabilities = {k: v / tries * 100 for k, v in results.items()}
    return probabilities
