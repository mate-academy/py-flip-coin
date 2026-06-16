import random


def flip_coin() -> dict:
    results = {k: v for k, v in enumerate([0] * 11)}
    for i in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1
        results[heads] += 1
    res_percent = {k: v / 100 for (k, v) in results.items()}
    return res_percent
