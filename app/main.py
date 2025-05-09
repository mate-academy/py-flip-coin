import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(
        trials: int = 10000, flips_per_trial: int = 10
) -> Dict[int, float]:
    results: Dict[int, int] = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads_count = (
            sum(random.choice([0, 1]) for _ in range(flips_per_trial))
        )
        results[heads_count] += 1

    # Конвертуємо в проценти
    return {k: round((v / trials) * 100, 2) for k, v in results.items()}


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    head_counts = sorted(data.keys())
    percentages = [data[count] for count in head_counts]

    plt.plot(head_counts, percentages, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.show()


# Використання
distribution = flip_coin()
print(distribution)
draw_gaussian_distribution_graph(distribution)
