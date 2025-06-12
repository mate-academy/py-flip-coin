import random
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> Dict[int, float]:
    result: Dict[int, int] = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        result[heads] += 1

    percentage_result: Dict[int, float] = {
        k: round((v / trials) * 100, 2) for k, v in result.items()
    }

    return percentage_result


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    keys = sorted(data.keys())
    values = [data[k] for k in keys]

    plt.figure(figsize=(10, 5))
    plt.plot(keys, values, marker="o", linestyle="-", color="skyblue")
    plt.title("Distribution of Heads in 10 Coin Flips (10,000+ Trials)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.xticks(range(11))  # від 0 до 10
    plt.show()


if __name__ == "__main__":
    stats = flip_coin()
    print(stats)
    draw_gaussian_distribution_graph(stats)
