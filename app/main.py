import random


def flip_coin() -> dict:
    simulations_amount = 10000
    result = {i: 0.00 for i in range(11)}
    i = 0
    heads = 0
    while i != simulations_amount:
        heads = 0
        for _ in range(10):
            if random.choice([1, 0]) == 1:
                heads += 1
        result[heads] += 1
        i += 1
    for key in result:
        result[key] = round((result[key] / simulations_amount) * 100, 2)

    return result
