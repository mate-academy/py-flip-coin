import random
from typing import Dict, List
import matplotlib.pyplot as plt


def flip_coin(num_flips: int = 10,
              num_cases: int = 10000)\
        -> Dict[int, float]:

    results: Dict[int, int] = \
        {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        heads_count = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                heads_count += 1
        results[heads_count] += 1

    percentages: Dict[int, float] = {
        k: round((v / num_cases) * 100, 2) for k,
        v in results.items()
    }

    return percentages


def draw_gaussian_distribution_graph(
        distribution: Dict[int, float],
        num_flips: int = 10)\
        -> None:

    heads_counts: List[int] = list(distribution.keys())
    percentages: List[float] = list(distribution.values())

    fig, ax = plt.subplots(figsize=(10, 6))

    bar_collection = ax.bar(heads_counts,
                            percentages,
                            color="skyblue",
                            edgecolor="black",
                            alpha=0.7)

    ax.set_xlabel("Number of Heads", fontsize=12)
    ax.set_ylabel("Percentage (%)", fontsize=12)
    ax.set_title(f"Gaussian Distribution of Coin Flips "
                 f"({num_flips} flips per case)",
                 fontsize=14,
                 fontweight="bold")

    ax.set_xticks(range(0, num_flips + 1))

    ax.grid(axis="y", alpha=0.3, linestyle="--")

    for individual_bar in bar_collection:
        bar_height = individual_bar.get_height()
        bar_center_x = individual_bar.get_x() + individual_bar.get_width() / 2
        ax.text(bar_center_x, bar_height + 0.1,
                f"{bar_height:.2f}%", ha="center", va="bottom", fontsize=9)

    expected_value = num_flips / 2
    ax.axvline(x=expected_value, color="red", linestyle="--", alpha=0.7,
               label=f"Expected Value ({expected_value} heads)")

    ax.legend()

    plt.tight_layout()

    plt.show()


def main() -> None:

    distribution = flip_coin()

    print("Coin Flip Distribution (10 flips per case, 10000 cases):")
    print(distribution)

    draw_gaussian_distribution_graph(distribution)


if __name__ == "__main__":
    main()
