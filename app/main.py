import random


def flip_coin() -> dict:
    result = {num: 0 for num in range(11)}

    for i in range(10000):
        number = 0
        for i in range(10):
            if random.randint(1, 2) == 1:
                number += 1
        result[number] += 1

    return {key: value / 100 for key, value in result.items()}
