import random


def flip_coin():
    data = {i: 0 for i in range(11)}
    for _ in range(10_000):
        count = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                count += 1
        data[count] += 1
    return {key: value / 100 for key, value in data.items()}
