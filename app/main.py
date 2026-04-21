import random


def flip_coin() -> dict:
    flipping_amount = 100_000
    results = {i: 0 for i in range(11)}

    for side in range(flipping_amount):
        heads = 0
        for flip in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] += 1

    for key in results:
        results[key] = (results[key] / flipping_amount) * 100

    return results
