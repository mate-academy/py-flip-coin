import random


def flip_coin() -> dict:
    result = {x: 0 for x in range(11)}

    trials = 10000
    for _ in range(trials):
        count = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            count += flip

        result[count] += 1

    percentage = {key: (value / trials) * 100 for key, value in result.items()}

    return percentage
