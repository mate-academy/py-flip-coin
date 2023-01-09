from random import choice
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    distribution = {}
    times = []
    for _ in range(10000):
        sample = [choice(["head", "tail"]) for _ in range(10)]
        times.append(sample.count("head"))
    for i in range(11):
        distribution[i] = round(times.count(i) / 100, 2)
    return distribution


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.plot(distribution.keys(), distribution.values())
    plt.show()
