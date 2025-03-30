import random


def flip_coin() -> dict:
    results = {}
    cases = 10000
    for _ in range(cases):
        count = 0
        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                count += 1
        results[count] = results.get(count, 0) + 1
    percentages = {key: value / cases * 100 for key, value in results.items()}
    return percentages
