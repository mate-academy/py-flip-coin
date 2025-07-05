import random
from typing import Dict


def flip_coin(trials: int = 10000) -> Dict[int, float]:
    """
    Simulates flipping a fair coin 10 times, repeated `trials` times.
    Returns a dictionary where:
      keys = 0..10 (number of heads)
      values = percentages rounded to 2 decimal places
    """
    counts = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        counts[heads] += 1

    percentages = {k: round((v / trials) * 100, 2) for k, v in counts.items()}
    return percentages


def draw_gaussian_distribution_graph(percentages: Dict[int, float]) -> None:
    """
    Draws a line chart of the heads distribution and saves as PNG.
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    head_counts = list(percentages.keys())
    percentages_list = list(percentages.values())

    plt.plot(
        head_counts,
        percentages_list,
        color="blue",
        marker="o",
        linestyle="-",
        linewidth=2
    )
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig("distribution.png")
    print("Line graph saved as distribution.png")

if __name__ == "__main__":
    results = flip_coin()
    print(results)
    draw_gaussian_distribution_graph(results)
