import random


def flip_coin() -> dict:
    result_flip_heads = []
    for _ in range(1, 10001):
        flips = [random.choice(["tails", "heads"]) for _ in range(1, 11)]
        flips_heads_count = flips.count("heads")
        result_flip_heads.append(flips_heads_count)
    return {
        i: result_flip_heads.count(i)
        / len(result_flip_heads)
        * 100 for i in range(11)
    }
