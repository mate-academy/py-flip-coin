import random


def flip_coin(simulations: int = 10000) -> dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(simulations):
        heads = 0
        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads += 1
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / simulations * 100, 2)

    return results
