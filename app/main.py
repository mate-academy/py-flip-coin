import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    num_experiments = 10000

    for _ in range(num_experiments):
        heads_count = 0
        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads_count += 1
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / num_experiments) * 100, 2)

    return results
