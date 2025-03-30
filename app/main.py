import random


def flip_coin() -> dict:
    drop_count = {}
    for test in range(10000):
        choices = []
        for i in range(10):
            choices.append(random.choice([0, 1]))
        head_count = choices.count(1)
        if not drop_count.get(head_count):
            drop_count[head_count] = 1
            continue
        drop_count[head_count] += 1
        del choices
    result = {idx: value / 100 for idx, value in drop_count.items()}
    return result
