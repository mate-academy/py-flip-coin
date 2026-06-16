import random


def flip_coin() -> dict:

    result = {i: 0 for i in range(11)}

    for i in range(10000):
        count = sum(random.choice([0, 1]) for i in range(10))
        result[count] += 1

    result = {k: round(((v / 10000) * 100), 2) for k, v in result.items()}

    return result


def draw_gaussian_distribution_graph(graph: dict) -> None:
    import matplotlib.pyplot as plt
    import numpy as np

    x_coor = np.array([number for number in graph.keys()])
    y_coor = np.array([number for number in graph.values()])

    plt.plot(x_coor, y_coor)
    plt.show()
