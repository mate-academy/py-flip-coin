import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / 10000 * 100, 2)

    return results


def draw_gaussian_distribution_graph(results: Dict[int, float]) -> None:
    plt.bar(results.keys(), results.values())
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()


results = flip_coin()
print(results)

draw_gaussian_distribution_graph(results)
