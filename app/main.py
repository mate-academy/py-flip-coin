import random


def flip_coin() -> dict:

    total_experiments = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(total_experiments):
        quantidade_de_caras = 0

        for _ in range(10):
            if random.randint(0, 1) == 1:
                quantidade_de_caras += 1

        results[quantidade_de_caras] += 1

    for key in results:
        results[key] = round((results[key] / total_experiments) * 100, 2)

    return results
