import random


def flip_coin() -> dict:
    heads_count = {i: 0 for i in range(11)}
    for _ in range(10_000):
        count = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                count += 1
        heads_count[count] += 1
    result_dict = {
        key: round((value / 10_000) * 100, 2)
        for key, value in heads_count.items()
    }
    return result_dict
