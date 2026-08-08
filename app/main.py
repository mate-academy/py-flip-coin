import matplotlib.pyplot as plt
import random


def flip_coin(experiments: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(experiments):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] += 1

    for per in results:
        results[per] = round((results[per] / experiments) * 100, 2)

    return results


def draw_gaussian_distribution_graph(dot: dict) -> None:
    for x_key, y_value in dot.items():
        x_coord = x_key.keys()
        y_coord = y_value.values()
        plt.plot(x_coord, y_coord)
    plt.show()
