import random


def flip_coin() -> dict[int, float]:
    result: dict[int, float] = {i: 0 for i in range(11)}
    trials: int = 10000
    for _ in range(trials):
        heads: int = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        result[heads] += 1
    for key in result:
        result[key] = (result[key] / trials) * 100
    return result
