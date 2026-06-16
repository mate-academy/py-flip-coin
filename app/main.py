import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_dict = {}
    for i in range(11):
        result_dict[i] = 0

    quantity_experiments = 10000
    for experiment in range(quantity_experiments):
        quantity_heads = sum(random.randint(0, 1) for _ in range(10))
        result_dict[quantity_heads] += 1

    for i in range(11):
        result_dict[i] = (
            round(result_dict[i] * 100 / quantity_experiments, 2))
    return result_dict


def draw_gaussian_distribution_graph(result_dict: dict) -> None:
    head_counts = list(result_dict.keys())
    drop_persentage = list(result_dict.values())
    plt.plot(head_counts, drop_persentage, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(np.arange(0, 10, 1))
    ticks = np.arange(0, 100, 5)
    labels = [str(t) if t % 10 == 0 else "" for t in ticks]
    plt.gca().set_yticks(ticks)
    plt.gca().set_yticklabels(labels)
    plt.show()
