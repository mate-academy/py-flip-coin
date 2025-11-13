import random
from typing import Dict, Union
import matplotlib.pyplot as plt


def flip_coin(
        num_cases: int = 10000,
        num_flips: int = 10) -> Dict[int, Union[int, float]]:
    results_count: Dict[int, int] = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        heads_count: int = sum(
            random.randint(0, 1) for _ in range(num_flips))
        results_count[heads_count] += 1

    percentage_results: Dict[int, Union[int, float]] = {
        heads: round((count / num_cases) * 100, 2)
        for heads, count in results_count.items()
    }

    return percentage_results


def draw_gaussian_distribution_graph(
        results: Dict[int, Union[int, float]]) -> None:
    heads_counts = list(results.keys())
    percentages = list(results.values())
    plt.figure(figsize=(10, 6))
    plt.plot(
        heads_counts,
        percentages,
        marker="o",
        linestyle="-",
        color="blue")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(heads_counts)
    plt.grid(axis="y", linestyle="--")
    plt.show()
