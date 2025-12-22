# write your code here
import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    possibilities = ["head", "tail"]
    results = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
        6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for _ in range(10000):
        base_list = []
        for i in range(10):
            base_list.append(random.choice(possibilities))
        results[base_list.count("head")] += 1

    pct_drop = []
    for result in results.values():
        pct_drop.append(result / 100)

    pct_results = {}
    for i in range(0, 11):
        pct_results[i] = pct_drop[i]

    xpoints = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ypoints = np.array(pct_drop)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(xpoints, ypoints)
    plt.savefig("Gaussian distribution")
    return pct_results
