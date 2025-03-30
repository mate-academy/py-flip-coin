import random


def flip_coin(num_trials: int = 10000) -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        num_heads = sum(random.choice([0, 1]) for _ in range(10))
        result[num_heads] += 1

    for key in result:
        result[key] = (result[key] / num_trials) * 100

    return result
