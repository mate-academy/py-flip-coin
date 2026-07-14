import random
from typing import Dict, List, Optional


def flip_coin(trials: int = 10000, flips: int = 10) -> Dict[int, float]:
    results: Dict[int, float] = {index: 0 for index in range(flips + 1)}
    for _ in range(trials):
        heads_count: int = sum(random.choice([0, 1]) for _ in range(flips))
        results[heads_count] += 1
    for index in results:
        results[index] = round(results[index] / trials * 100, 2)
    return results


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> Optional[None]:
    import matplotlib.pyplot as plt
    heads_values: List[int] = list(data.keys())
    drop_percentages: List[float] = list(data.values())
    plt.plot(heads_values, drop_percentages, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()
    return None
