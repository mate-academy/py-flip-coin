import random


def flip_coin(trials: int = 10000,
              flips: int = 10) -> dict[int, float]:
    flip_result = {i: 0 for i in range(0, flips + 1)}

    for _ in range(trials):
        head = (sum(random.choice[0, 1]) for _ in range(flips))
        flip_result[head] += 1

    for key in flip_result:
        flip_result[key] = (flip_result[key] / trials) * 100

    return flip_result
