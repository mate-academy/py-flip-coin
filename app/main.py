import random


def flip_coin() -> dict:
    coin = ["head", "tail"]
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice(coin) == "head":
                heads += 1
        results[heads] += 1

    d1 = {
        heads: round((count / 10000) * 100, 2)
        for heads, count in results.items()
    }
    return d1


def draw_gaussian_distribution_graph(d1: dict) -> None:
    import matplotlib.pyplot as plt
    import numpy as np
    x_point = np.arange(0, 11)
    y_point = [d1[num_heads] for num_heads in x_point]

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.plot(x_point, y_point)

    plt.show()
