import random


def flip_coin() -> dict:
    possibility_of_head_drop = {n: 0 for n in range(11)}

    for _ in range(10000):
        number_of_head_drop = 0
        for _ in range(10):
            drop = random.randint(0, 1)
            number_of_head_drop += drop
        possibility_of_head_drop[number_of_head_drop] += 1

    for times in possibility_of_head_drop:
        possibility_of_head_drop[times] = possibility_of_head_drop[times] / 100

    return possibility_of_head_drop
