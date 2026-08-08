import random


def flip_coin() -> dict:
    num_cases = 10000
    coin = ["head", "tail"]

    results = {i: 0 for i in range(11)}
    for _ in range(num_cases):
        heads = 0
        for _ in range(10):
            flip = random.choice(coin)
            if flip == "head":
                heads += 1
        results[heads] += 1

    distribution = {
        heads: round((count / num_cases) * 100, 2)
        for heads, count in results.items()
    }
    return distribution


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    import matplotlib.pyplot as plt
    import numpy as np
    x_points = np.arange(0, 11)
    y_points = [distribution[num_heads] for num_heads in x_points]

    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads Dropped")
    plt.plot(x_points, y_points)

    plt.show()
