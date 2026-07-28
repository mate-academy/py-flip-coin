import random


def flip_coin() -> dict:
    probability = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for i in range(10000):
        heads_dropped = 0
        for _ in range(10):
            heads_dropped += random.randint(0, 1)

        probability[heads_dropped] += 1

    for i in probability:
        probability[i] = round(probability[i] / 10000 * 100, 2)

    return probability
