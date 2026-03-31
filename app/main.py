import random


def flip_coin() -> dict:
    total_experiments = 10000
    flips_per_experiment = 10

    heads_count = {i: 0 for i in range(0, 11)}

    for _ in range(total_experiments):
        heads = sum(random.choice([0, 1])
                    for _ in range(flips_per_experiment))
        heads_count[heads] += 1

    for key in heads_count:
        heads_count[key] = (heads_count[key] / total_experiments) * 100

    return heads_count
