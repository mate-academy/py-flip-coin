import random
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000,
              flips_per_case: int = 10) -> dict[int, float]:
    """
    Run a coin-flip simulation.

    Args:
        cases: Number of experiments to run.
        flips_per_case: Number of coin flips per experiment.

    Returns:
        Dictionary mapping number of heads (0..flips_per_case) to
        percentage of cases (rounded to 2 decimals).
    """
    counts = [0] * (flips_per_case + 1)

    for _ in range(cases):
        heads = 0
        for _ in range(flips_per_case):
            if random.random() < 0.5:
                heads += 1
        counts[heads] += 1

    return {
        i: round(counts[i] * 100 / cases, 2)
        for i in range(flips_per_case + 1)
    }


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    """
    Draw a bar chart showing the distribution of heads.

    Args:
        distribution: Dictionary mapping number of heads to percentage.
    """
    xs = sorted(distribution.keys())
    ys = [distribution[x] for x in xs]

    plt.bar(xs, ys)
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads (out of 10)")
    plt.ylabel("Percentage of Cases")
    plt.xticks(xs)
    plt.show()


if __name__ == "__main__":
    dist = flip_coin(100_000, 10)
    print(dist)
    draw_gaussian_distribution_graph(dist)
