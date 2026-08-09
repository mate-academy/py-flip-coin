import random


def flip_coin() -> dict:
    head_count = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    for _ in range(0, 10000):
        head_times = 0
        for _ in range(0, 10):
            flip = random.choice([1, 0])
            if flip == 1:
                head_times += 1
        head_count[head_times] += 1
    head_percentages = {}
    for key in head_count:
        head_percentages[key] = round((head_count[key] / 10000) * 100, 2)
    return head_percentages
