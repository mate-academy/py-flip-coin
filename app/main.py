import random


def flip_coin() -> dict:
    results = {count: 0.0 for count in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice(["Heads", "Tails"]) == "Heads":
                heads += 1
        results[heads] += 1
    for key in results:
        results[key] = round(results[key] / 10000 * 100, 2)
    return results
