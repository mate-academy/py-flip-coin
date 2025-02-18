import random


def flip_coin() -> dict[int: float]:
    result = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0,
              5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0}
    for case in range(0, 10000):
        heads_count = 0
        for flip in range(0, 10):
            if random.gauss(0.5, 0.5) > 0.5:
                heads_count += 1
        result[heads_count] += 0.01
    for flip in range(0, 11):
        result[flip] = round(result[flip], 4)
    return result

