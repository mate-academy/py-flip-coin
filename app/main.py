import random
from typing import Dict


def flip_coin() -> Dict[int, float]:
    results = {heads: 0 for heads in range(11)}

    for _ in range(10000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        results[heads] += 1

    return {heads: count / 100 for heads, count in results.items()}


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt

    distribution = flip_coin()
    plt.bar(distribution.keys(), distribution.values())
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Coin flip distribution")
    plt.show()
