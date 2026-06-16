import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                count += 1
        result_dict[count] += 1
    result_dict = {k: v / 100 for k, v in result_dict.items()}
    return result_dict
