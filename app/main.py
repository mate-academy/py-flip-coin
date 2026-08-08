import random


def flip_coin(flips_number: int = 10000) -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(flips_number):
        head = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                head += 1
        result[head] += 1
    result = {key: value / 100 for key, value in result.items()}
    return result
