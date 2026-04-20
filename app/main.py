import random


def flip_coin() -> dict:
    num = 10
    trs = 10000
    trials = [
        sum([random.randint(0, 1) for i in range(num)]) for j in range(trs)
    ]
    freq = [trials.count(k) for k in range(num + 1)]
    percentage = {key: value / 100 for key, value in enumerate(freq)}
    return percentage
