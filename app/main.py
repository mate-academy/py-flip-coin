import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    results = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        results[heads] += 1

    for result in results:
        results[result] = round(results[result] / trials * 100, 2)

    return results


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_values = list(result.keys())
    y_values = list(result.values())

    plt.figure(figsize=(8, 5))
    plt.bar(x_values, y_values, color="skyblue", edgecolor="black")

    plt.title("Gaussian distribution", fontsize=14)
    plt.xlabel("Heads count", fontsize=12)
    plt.ylabel("Drop percentage %", fontsize=12)
    plt.xticks(range(len(x_values)))
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.show()
