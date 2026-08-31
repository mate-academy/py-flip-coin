
import random


def flip_coin(num_trials: int = 10000) -> dict:
    counts = {
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
        10: 0
    }
    for trial in range(num_trials):
        eagle = 0
        for i in range(10):
            result = random.randint(0, 1)
            if result == 1:
                eagle += 1
        counts[eagle] += 1
    percentages = {}
    for key in counts:
        percentages[key] = (counts[key] / num_trials) * 100
    return percentages
