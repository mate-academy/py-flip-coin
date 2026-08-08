import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    results = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
        5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for _ in range(10000):
        heads = 0
        for _ in range(0, 10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1
        results[heads] += 0.01
    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    xpoints = []
    ypoints = []
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    for key in results:
        xpoints.append(key)
        ypoints.append(results[key])

    plt.plot(np.array(xpoints), np.array(ypoints))
    plt.show()
