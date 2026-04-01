import random


def flip_coin(cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    return {
        k: round(v / cases * 100, 2)
        for k, v in results.items()
    }
