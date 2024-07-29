import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    outcome = {i: 0 for i in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        outcome[heads_count] += 1

    percentages = {key: (value / total_cases) * 100
                   for key, value in outcome.items()}
    return percentages


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    keys = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(8, 6))
    plt.plot(keys, values, color="blue",
             linestyle="-",
             linewidth=2,
             markersize=8)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.xticks(keys)
    plt.grid(True)
    plt.show()


result = flip_coin()
draw_gaussian_distribution_graph(result)
print(result)
