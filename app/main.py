import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(trials: int = 10000) -> Dict[int, float]:
    head_counts: Dict[int, float] = {i: 0.0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        head_counts[heads] += 1

    for key in head_counts:
        head_counts[key] = round((head_counts[key] / trials) * 100, 2)

    return head_counts


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    keys = list(distribution.keys())
    values = list(distribution.values())

    plt.plot(keys, values, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()


results = flip_coin()
print(results)
draw_gaussian_distribution_graph(results)
