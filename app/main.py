import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for i in range(10000):
        heads = 0
        for i in range(10):
            flip = random.choice([0, 1])
            if flip == 1:
                heads += 1
        result[heads] += 1
    percent = {heads: round(count / 10000 * 100, 2) for heads,
               count in result.items()}
    return percent


def draw_gaussian_distribution_graph() -> None:
    graph = flip_coin()

    plt.bar(graph.keys(), graph.values())

    plt.show()
