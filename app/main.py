import random


def flip_coin() -> dict:
    result = {head: 0 for head in range(11)}
    for _ in range(10000):
        count_of_heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 0:
                count_of_heads += 1
        result[count_of_heads] += 1
    result = {
        head_of_ten: count_heads / 100
        for head_of_ten, count_heads in result.items()
    }
    return result
