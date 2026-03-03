import random
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin(simulations: int = 10000) -> Dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(simulations):
        heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1

    percentages = {}
    for key, value in results.items():
        percent = (value / simulations) * 100
        percentages[key] = round(percent, 2)

    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x = list(data.keys())
    y = list(data.values())

    plt.bar(x, y)
    plt.xlabel("Number of Heads (0-10)")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Flip Distribution (10 flips)")
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
