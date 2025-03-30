import random


def flip_coin() -> dict:
    flip_list = [0 for _ in range(11)]

    for _ in range(10000):
        count = 0

        for _ in range(10):
            if random.randint(0, 1):
                count += 1

        flip_list[count] += 1

    return {num: flip_list[num] / 100 for num in range(11)}
