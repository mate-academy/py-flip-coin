import random


def flip_coin(attempts: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(attempts):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / attempts) * 100

    return dict(results)
