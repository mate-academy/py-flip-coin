from random import choice


def flip_coin() -> dict:
    result_dict = {
        0: 0,
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

    for _ in range(10000):
        head_count = 0
        for _ in range(10):
            if choice([True, False]) is True:
                head_count += 1
        result_dict[head_count] += (1 / 100)

    return result_dict
