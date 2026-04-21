import random
import matplotlib.pyplot as plt
from typing import Callable


def flip_coin() -> dict:
    sim_runs = 10000
    max_flips = 10
    rd = random.Random()
    flip_stats = {key: 0 for key in range(11)}

    for sim_run in range(sim_runs):
        counter = 0
        for flip in range(max_flips):
            if rd.randint(0, 1) == 1:
                counter += 1

        flip_stats[counter] += 1

    return {
        key: round(value / sim_runs * 100, 2)
        for key, value in flip_stats.items()
    }


def draw_gaussian_distribution_graph(flips: Callable) -> None:
    data = flips()
    head_count = list(data.keys())
    percents = list(data.values())

    plt.plot(head_count, percents)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))
    plt.show()
