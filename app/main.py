import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(simulations: int = 10000) -> dict:
    flip_stat = defaultdict(int)

    for _ in range(simulations):
        heads_flip = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                heads_flip += 1

        flip_stat[heads_flip] += 1

    for key in flip_stat:
        flip_stat[key] = round(flip_stat[key] * 100 / simulations, 2)

    return dict(flip_stat)


data = flip_coin()


def draw_gaussian_distribution_graph(data: dict) -> None:
    point_x = sorted(data.keys())
    point_y = [data[k] for k in point_x]

    plt.bar(point_x, point_y, color="blue", edgecolor="black")
    plt.title("Heads in 10 coin flips in 10000 cases")
    plt.xlabel("Heads count")
    plt.ylabel("%")
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.show()
