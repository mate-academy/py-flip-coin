import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000, flips: int = 10) -> dict[int, float]:
    results: dict[int, int] = {i: 0 for i in range(flips + 1)}
    for _ in range(trials):
        heads: int = sum(random.choice([0, 1]) for _ in range(flips))
        results[heads] += 1
    percentages: dict[int, float] = {
        k: round(v / trials * 100, 2) for k, v in results.items()
    }
    return percentages


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    keys: list[int] = list(distribution.keys())
    values: list[float] = list(distribution.values())
    plt.figure(figsize=(8, 5))
    plt.bar(keys, values, color="skyblue", edgecolor="black")
    plt.plot(keys, values, color="red", marker="o")
    plt.title("Gaussian Distribution of Coin Flips (10 flips)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(range(0, 11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    distribution: dict[int, float] = flip_coin()
    print(distribution)
    draw_gaussian_distribution_graph(distribution)
