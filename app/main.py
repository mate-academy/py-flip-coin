import random


def flip_coin() -> dict:
    num_flips = 10

    outcomes = [0] * (num_flips + 1)

    for _ in range(10000):
        num_heads = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                num_heads += 1
        outcomes[num_heads] += 1

    return {i: (count / 10000) * 100 for i, count in enumerate(outcomes)}
