import random
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin():
    head_appearing_frequency = Counter(
        [random.choice(["head", "tail"]) for _ in range(10)].count("head")
        for _ in range(10000)
    )

    head_appearing_percentage = {
        key: round(value / 100)
        for key, value in sorted(head_appearing_frequency.items())
    }

    return head_appearing_percentage


def draw_gaussian_distribution_graph(percentage_dict):
    fig, ax = plt.subplots()
    ax.plot(percentage_dict.keys(), percentage_dict.values())
    ax.set_title('Gaussian distribution')
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage %")
    ax.set_ylim([0, 100])
    plt.show()
