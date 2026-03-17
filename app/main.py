import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(trials: int = 10000, flips: int = 10) -> Dict:
    results: Dict[int, int] = {count: 0 for count in range(flips + 1)}
    for _ in range(trials):
        heads_count: int = sum(random.choice([0, 1]) for _ in range(flips))
        results[heads_count] += 1
    percentages: Dict[int, float] = {
        count: round(results[count] / trials * 100, 2) for count in results
    }
    return percentages


def draw_gaussian_distribution_graph(
        trials: int = 10000,
        flips: int = 10
) -> None:
    data: Dict[int, float] = flip_coin(trials, flips)

    plt.figure(figsize=(8, 5))
    plt.plot(list(data.keys()), list(data.values()), marker="o", color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()
