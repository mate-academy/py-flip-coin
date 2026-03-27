import random

heads = 1


def flip_coin() -> dict:
    result = {}
    for _ in range(15000):
        heads_counter = 0

        for _ in range(1, 11):
            flip = random.randint(0, 1)
            if flip == heads:
                heads_counter += 1
        result[heads_counter] = result.get(heads_counter, 0) + 1

    for key, value in result.items():
        result[key] = (value / 15000) * 100

    return result
