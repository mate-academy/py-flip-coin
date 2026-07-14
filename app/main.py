import random


def flip_coin() -> dict[int, float]:
    iterations = 10000
    result: dict[int, float] = {}
    score: dict[int, int] = {iteration: 0 for iteration in range(11)}
    for iteration in range(iterations):
        heads_count = 0
        for _ in range(10):
            if random.choice([0, 1]) == 1:
                heads_count += 1
            score[heads_count] += 1
    for iteration in score:
        result[iteration] = score[iteration] * 100 / iterations
    return result
