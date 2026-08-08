import random


def flip_coin() -> None:
    results = {}
    cases = 10000

    for i in range(cases):
        flips = [random.choice(["Eagle", "Tail"]) for _ in range(10)]
        eagle = flips.count("Eagle")

        if eagle not in results:
            results[eagle] = 0
        results[eagle] += 1

    for key in results:
        results[key] = (results[key] / cases) * 100

    return results
