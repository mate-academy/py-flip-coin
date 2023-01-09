from random import randint


def flip_coin() -> dict:
    head_dropped = {i: 0 for i in range(11)}
    for i in range(10000):
        count = 0
        for _ in range(10):
            if randint(0, 1) == 1:
                count += 1
        head_dropped[count] += 1

    result = {key: value / 100 for key, value in head_dropped.items()}
    return result
