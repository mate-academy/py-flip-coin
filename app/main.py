import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    for heads in results:
        results[heads] = (results[heads] / total_cases) * 100

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_values = list(results.keys())
    y_values = list(results.values())

    plt.plot(x_values, y_values, marker="o")

    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")

    plt.grid(True)

    plt.show()
