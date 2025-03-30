import random


def flip_coin() -> dict:
    head_possibility = {}
    for _ in range(10000):
        flips = sum(1 if random.random() > 0.5 else 0 for _ in range(10))
        if flips in head_possibility:
            head_possibility[flips] += 1
        else:
            head_possibility[flips] = 1
    for key, value in head_possibility.items():
        head_possibility[key] = round(value / 10000 * 100, 2)

    list_key_sort = list(head_possibility.keys())
    list_key_sort.sort()
    return {key: head_possibility[key] for key in list_key_sort}
