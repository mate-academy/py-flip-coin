import random


def flip_coin():
    result = {}
    for _ in range(10000):
        how_many = 0
        for i in range(10):
            coin = random.randint(0, 1)
            if coin == 0:
                how_many += 1
        if how_many in result:
            result[how_many] += 1
        else:
            result[how_many] = 1
    for key, value in result.items():
        result[key] = round(value / 10000 * 100, 2)
    return result
