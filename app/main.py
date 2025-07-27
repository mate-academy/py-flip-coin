import random


def flip_coin() -> dict:
    percents_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                     6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        heads_count = sum(random.getrandbits(1) for _ in range(10))
        percents_dict[heads_count] += 1

    return {key: value / 100 for key, value in percents_dict.items()}
