import random


def flip_coin() -> dict:
    temporary_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        flip = sum(random.randint(0, 1) for _ in range(10))
        temporary_dict[flip] += 1
    percentage_dict = {
        value: (count / 10000) * 100
        for value, count in temporary_dict.items()
    }
    return percentage_dict
