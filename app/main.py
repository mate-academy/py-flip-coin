import random


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    results = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads_count = sum(
            random.choice(["H", "T"]) == "H" for _ in range(flips)
        )
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)

    return results


distribution = flip_coin()
print(distribution)
