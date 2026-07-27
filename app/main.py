import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            result = random.choice(["heads", "tails"])
            if result == "heads":
                heads_count += 1
        if heads_count in results:
            results[heads_count] += 1
        elif heads_count not in results:
            results[heads_count] = 1
    for key in results:
        results[key] = (results[key] / 10000) * 100
    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_axis = list(results.keys())
    y_axis = list(results.values())
    plt.bar(x_axis, y_axis)
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Probability")
    plt.show()
