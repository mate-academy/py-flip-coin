import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    total_trials: int = 10000
    head_counts: dict[int, int] = {i: 0 for i in range(11)}

    for _ in range(total_trials):
        heads_in_trial: int = sum(random.choice([0, 1]) for _ in range(10))
        head_counts[heads_in_trial] += 1

    percentage_results: dict[int, float] = {
        count: round((num / total_trials) * 100, 2)
        for count, num in head_counts.items()
    }

    return percentage_results


def draw_gaussian_distribution_graph() -> None:
    results: dict[int, float] = flip_coin()
    head_values: list[int] = list(results.keys())
    percentage_values: list[float] = list(results.values())

    plt.bar(
        head_values,
        percentage_values,
        color="skyblue",
        edgecolor="black"
    )
    plt.xlabel("Heads in 10 Coin Flips")
    plt.ylabel("Percentage (%)")
    plt.title(
        "Distribution of Heads in 10 Coin Flips\n(10,000 Trials)"
    )
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(range(11))
    plt.tight_layout()
    plt.show()
