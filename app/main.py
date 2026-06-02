import random
import matplotlib.pyplot as plt
import numpy as np


def toss_10_times() -> str:
    tosses = []
    
    for _ in range(10):
        tosses.append(random.choice(["head", "tail"]))

    return tosses.count("head")


def flip_coin() -> dict:
    stats = {x: 0 for x in range(11)}

    for _ in range(10000):
        stats[toss_10_times()] += 1

    for key in stats:
        stats[key] = stats[key] / 100

    return stats


def draw_gaussian_distribution_graph() -> None:
    probabilities = flip_coin()

    xpoints = np.array(list(probabilities.keys()))
    ypoints = np.array(list(probabilities.values()))

    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
