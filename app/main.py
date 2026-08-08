import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        count_heads = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                count_heads += 1

        result[count_heads] += 1

    for key in result:
        result[key] = (result[key] / 10000) * 100

    return result
