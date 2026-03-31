import random


def flip_coin() -> dict:
    trials = 10000
    heads_count = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        heads_count[heads] += 1

    heads_percentage = {k: (v / trials) * 100 for k, v in heads_count.items()}

    return heads_percentage
