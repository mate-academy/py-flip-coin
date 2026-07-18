import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads_count += 1
        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / 100, 2)

    return results
