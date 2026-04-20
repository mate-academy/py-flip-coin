from random import choices
import numpy as np
import matplotlib.pyplot as plt
import sys


def flip_coin() -> dict:
    head_percentage: dict[int, float] = {i: 0 for i in range(11)}

    for _ in range(10000):
        head_count = choices(["Head", "Tail"], k=10).count("Head")
        head_percentage[head_count] += 1

    for i in range(11):
        head_percentage[i] = round((head_percentage.get(i) / 10000) * 100, 2)
    return head_percentage


def draw_gaussian_distribution_graph() -> None:
    results_dict = flip_coin()
    x_values = np.array(list(results_dict.keys()))
    y_percentages = np.array(list(results_dict.values()))

    plt.plot(x_values, y_percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(x_values)
    plt.ylim(0, 100)
    plt.savefig("Extra.png")

    plt.savefig(sys.stdout.buffer)
    sys.stdout.flush()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
