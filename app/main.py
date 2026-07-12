import random


def flip_coin() -> dict[int, float]:
    iterations = 10000
    result: dict[int, float] = {}
    score: dict[int, int] = {iteration: 0 for iteration in range(10)}
    for iteration in range(iterations):
        for time in range(10):
            score[time] += random.choice([0, 1])
    for iteration in score:
        result[iteration] = score[iteration] * 100 / iterations
    return result
