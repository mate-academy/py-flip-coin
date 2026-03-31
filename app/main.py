import random


def flip_coin() -> dict:
    rounds = 10000
    result = {i: 0 for i in range(11)}

    for _ in range(rounds):
        heads_count = 0
        for _ in range(10):
            flip = random.choice([0, 1])
            heads_count += flip
        result[heads_count] += 1

    for key in result:
        result[key] = (result[key] / rounds) * 100

    return result
