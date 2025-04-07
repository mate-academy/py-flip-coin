import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_count = {
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
        10: 0,
    }
    conducts = 10000
    for _ in range(conducts):
        count_heads = 0
        for number in range(10):
            coin = random.choice(["heads", "tails"])
            if coin == "heads":
                count_heads += 1
        result_count[count_heads] += round(1 / conducts * 100, 2)
    for key in result_count:
        result_count[key] = round(result_count[key], 2)
    return result_count


xpoints = np.array([0, 10])
ypoints = np.array([0, 100])

plt.plot(flip_coin().keys(), flip_coin().values())
plt.show()
