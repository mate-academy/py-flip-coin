import random


def flip_coin():
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        count = 0
        for flip in range(10):
            if random.randint(1, 2) == 1:
                count += 1
        result[count] += 1
    result = {key: val / 100 for key, val in result.items()}
    return result
