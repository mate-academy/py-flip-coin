from random import randint


def flip_coin():
    heads_times = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            heads += randint(0, 1)
        heads_times[heads] += 1

    return {key: (value / 100) for key, value in heads_times.items()}
