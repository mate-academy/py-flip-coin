import random


def flip_coin(simulations: int = 10000) -> dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(simulations):
        heads = 0

        for _ in range(10):
            if random.choice([True, False]):
                heads += 1

        results[heads] += 1

    return {
        key: round((value / simulations) * 100, 2)
        for key, value in results.items()
    }
