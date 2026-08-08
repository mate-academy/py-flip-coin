import random
from typing import Dict


def flip_coin(cases: int = 10_000) -> Dict[int, float]:
    result = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0
        for _ in range(10):
            if random.choice((0, 1)) == 1:
                heads += 1
        result[heads] += 1

    for key in result:
        result[key] = round(result[key] / cases * 100, 2)

    return result


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    import matplotlib.pyplot as plt  # ← КЛЮЧОВИЙ МОМЕНТ

    heads = list(distribution.keys())
    percentages = list(distribution.values())

    plt.plot(heads, percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
