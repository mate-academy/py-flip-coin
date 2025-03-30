import random


def flip_coin() -> dict:
    result = [sum(random.randint(0, 1)
                  for _ in range(10)) for _ in range(10000)]
    counts = {i: result.count(i) for i in range(11)}
    probabilities = {key: round(value / 10000 * 100, 2)
                     for key, value in counts.items()}
    return probabilities
