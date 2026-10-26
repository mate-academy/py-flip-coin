import random
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin() -> Dict[int, float]:
    total_trials = 10000
    counts: Dict[int, int] = {i: 0 for i in range(11)}

    for _ in range(total_trials):
        # Flip a coin 10 times (0 for tails, 1 for heads)
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        counts[heads_count] += 1

    percentages: Dict[int, float] = {
        heads: round((count / total_trials) * 100, 2)
        for heads, count in counts.items()
    }

    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads_counts = list(data.keys())
    drop_percentages = list(data.values())

    plt.figure(figsize=(8, 6))
    plt.plot(heads_counts, drop_percentages, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(0, 11))

    plt.minorticks_on()
    plt.show()
