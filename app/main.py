import random


def flip_coin() -> dict:
    num_expiriance = 10000
    num_flip = 10
    result = {i: 0 for i in range(num_flip + 1)}

    for _ in range(num_expiriance):
        heads = sum(random.choice([0, 1]) for _ in range(num_flip))
        result[heads] += 1

    result = {k: (v / num_expiriance) * 100 for k, v in result.items()}
    return result
