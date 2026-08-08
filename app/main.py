import random


def flip_coin(trials: int = 10000, num_flips: int = 10) -> dict[int, float]:
    results = {}

    for _ in range(trials):
        heads = 0
        for _ in range(num_flips):
            if random.choice(["H", "T"]) == "H":
                heads += 1
        if heads not in results:
            results[heads] = 1
        else:
            results[heads] += 1

    for key in results:
        results[key] = (results[key] / trials) * 100

    return results
