import random


def flip_coin(numbers: int = 10000) -> dict:
    if numbers <= 0:
        return {i: 0.0 for i in range(11)}

    counts = [0] * 11
    for _ in range(numbers):
        heads = sum(random.randint(0, 1) for _ in range(10))
        counts[heads] += 1

    return {
        i: round(counts[i] / numbers * 100, 2)
        for i in range(11)
    }
