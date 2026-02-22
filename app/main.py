import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        number_of_tails = 0
        for _ in range(10):
            coin = random.randint(0, 1)
            if coin == 1:
                number_of_tails += 1
        result[number_of_tails] += 1
    return {
        k: (v / 10000) * 100
        for k, v in result.items()
    }


def draw_gaussian_distribution_graph():
    result = flip_coin()
    x = np.array([k for k, v in result.items()])
    y = np.array([v for k, v in result.items()])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.ylim(0, 100)
    plt.yticks(np.arange(0, 101, 10))
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
