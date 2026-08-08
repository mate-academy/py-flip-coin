import random


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
              6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    trials = 10000

    for _ in range(trials):
        heads_count = 0
        for _ in range(10):
            heads_count += random.randint(0, 1)

        result[heads_count] += 1

    for key in result:
        result[key] = (result[key] / trials) * 100

    return result
