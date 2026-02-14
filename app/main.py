import random
import matplotlib.pyplot as plt


def flip_coin(number: int = 10000) -> dict:
    counts = {i: 0 for i in range(11)}
    for _ in range(number):
        heads = 0
        for _ in range(10):
            heads += random.randint(0, 1)
        counts[heads] += 1
    return {i: round(counts[i] / number * 100, 2) for i in range(11)}


def draw_gaussian_distribution_graph(coords: dict) -> None:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 5))
    xpoints = list(coords.keys())
    ypoints = list(coords.values())
    plt.plot(xpoints, ypoints)
    plt.show()
