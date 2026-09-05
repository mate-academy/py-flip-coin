import random
import matplotlib.pyplot as plt


def flip_coin(n_cases: int = 10000, n_flips: int = 10) -> None:
    results = {i: 0 for i in range(n_flips + 1)}

    for _ in range(n_cases):
        heads = sum(random.choice([0, 1]) for _ in range(n_flips))
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] * 100 / n_cases, 2)
    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    plt.bar(results.keys(),
            results.values(),
            color="skyblue",
            edgecolor="black"
            )
    plt.title("Gaussian Distribution of Coin Tosses")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
