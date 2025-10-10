import random

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    results = {i: 0 for i in range(11)}  # Possible heads: 0 to 10

    for _ in range(trials):
        heads = sum(
            random.choice([0, 1]) for _ in range(10))  # Flip coin 10 times
        results[heads] += 1

    # Convert counts to percentages
    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(results) -> None:
    keys = list(results.keys())
    values = list(results.values())

    plt.bar(keys, values, color="skyblue", edgecolor="black")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.xticks(keys)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    print(results)
    draw_gaussian_distribution_graph(results)
