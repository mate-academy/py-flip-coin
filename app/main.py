import random


def flip_coin() -> dict:
    dict_flip = {0: 0, 1: 0, 2: 0,
                 3: 0, 4: 0, 5: 0, 6: 0,
                 7: 0, 8: 0, 9: 0, 10: 0}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            heads_count += random.choice([1, 0])
        dict_flip[heads_count] += 1

    for key in dict_flip:
        dict_flip[key] = (dict_flip[key] / 10000) * 100
    return dict_flip
