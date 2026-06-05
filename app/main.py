import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    result = {i: 0.0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            heads += random.randint(0, 1)
        result[heads] += 1
    for key in result:
        result[key] = result[key] * 100 / 10000
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    xpoints = result.keys()
    ypoints = result.values()
    plt.plot(xpoints, ypoints)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage%")
    plt.show()
