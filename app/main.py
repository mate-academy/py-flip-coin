import random


def flip_coin() -> dict:
    statistic_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                      5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for i in range(10000):
        head = 0
        for item in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                head += 1
        statistic_dict[head] += 1
    for key, value in statistic_dict.items():
        statistic_dict[key] = round(value / 10000 * 100, 2)
    return statistic_dict


print(flip_coin())
