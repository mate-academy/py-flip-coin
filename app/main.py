import random


def flip_coin():
    dict_flip_result = {i: 0 for i in range(11)}

    for i in range(10000):
        flips = [random.randint(0, 1) for x in range(10)]
        count = sum(flips)
        dict_flip_result[count] += 1 / 100

    return {key: int(value) for key, value in dict_flip_result.items()}
