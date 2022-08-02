import random


def flip_coin():
    stat_data = dict.fromkeys(range(11), 0)
    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(0, 1):
                count += 1
        stat_data[count] += 1
    for key in stat_data:
        stat_data[key] = stat_data[key] / 100
    return stat_data
