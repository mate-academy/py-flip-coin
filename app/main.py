from random import randint


def flip_coin() -> dict:
    distribution = {num: 0 for num in range(11)}

    for i in range(10000):
        heads_dropped = 0
        for ten_times in range(10):
            if randint(1, 2) == 1:
                heads_dropped += 1
        distribution[heads_dropped] += 1

    probabilities = {
        key: (value / 10000) * 100
        for key, value in distribution.items()
    }
    return probabilities
