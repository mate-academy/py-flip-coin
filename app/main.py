import random


def flip_coin() -> dict:
    result_dict = {0: 0.0, 1: 0.0, 2: 0.0,
                   3: 0.0, 4: 0.0, 5: 0.0,
                   6: 0.0, 7: 0.0, 8: 0.0,
                   9: 0.0, 10: 0.0}

    for _ in range(10000):
        head = 0
        for _ in range(10):
            if random.choice([0, 1]):
                head += 1
        result_dict[head] += 1 / 100

    result_dict = {key: round(value, 2) for key, value in result_dict.items()}

    return result_dict
