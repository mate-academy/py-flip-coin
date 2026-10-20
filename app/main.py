import random


def flip_coin() -> dict[int, float]:
    cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads_count = 0

        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] * 100 / cases, 2)

    return results
