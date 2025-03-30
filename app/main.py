import random


def flip_coin() -> dict:
    probability = {time: 0 for time in range(11)}

    for _ in range(10_000):
        counter = 0

        for _ in range(10):
            if random.randint(0, 1) == 1:
                counter += 1

        probability[counter] += 1

    result = {time: value / 100 for time, value in probability.items()}

    return result
