import random


def flip_coin() -> dict:
    num_of_experiments = 10000
    result = {0: 0,
              1: 0,
              2: 0,
              3: 0,
              4: 0,
              5: 0,
              6: 0,
              7: 0,
              8: 0,
              9: 0,
              10: 0}

    for _ in range(num_of_experiments):
        heads_count = 0
        for _ in range(10):
            heads_count += random.randint(0, 1)
        result[heads_count] += 1

    for key in result:
        result[key] = result[key] / 100

    return result
