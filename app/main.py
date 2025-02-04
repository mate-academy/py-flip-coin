import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(trials: int = 10000,
              flips: int = 10) -> dict[int, float]:
    flip_result = {i: 0 for i in range(0, flips + 1)}

    for _ in range(trials):
        head = sum(random.choice[0, 1]) for _ in range(flips)
        flip_result[head] += 1

    for key in flip_result:
        flip_result[key] = (flip_result[key] / trials) * 100

    return flip_result


def draw_gaussian_distribution_graph(flip_dict: dict) -> None:
    plt.plot(list(flip_dict.keys()), list(flip_dict.values()))
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.yticks(np.arange(0, 101, 10))
    plt.xticks(np.arange(0, 11, 1))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
