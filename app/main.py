import random


def flip_coin():
    dict1 = {i: 0 for i in range(11)}
    for i in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                count += 1
        dict1[count] += 1

    result = {key: value / 100 for key, value in dict1.items()}
    return result
