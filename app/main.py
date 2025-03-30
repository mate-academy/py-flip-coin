import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    times_flip = 10000

    for _ in range(times_flip):
        count = 0
        for _ in range(10):
            flip_coin = random.randint(0, 1)
            if flip_coin == 1:
                count += 1
        result[count] += 1

    for key, value in result.items():
        result[key] = value / times_flip * 100

    return result
