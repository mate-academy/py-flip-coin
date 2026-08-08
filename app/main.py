import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    tosses = 10_000

    results = {x: 0 for x in range(11)}

    for attempt in range(tosses):
        head = 0
        for toss in range(10):
            if random.randint(1, 2) == 1:
                head += 1
        results[head] += 1

    for key in results.keys():
        results[key] = round(results[key] / tosses * 100, 2)

    x_axc = np.array(list(results.keys()))
    y_axc = np.array(list(results.values()))

    plt.plot(x_axc, y_axc)
    plt.show()

    return results
