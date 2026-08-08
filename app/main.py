import random
import matplotlib.pyplot as plt
from collections import defaultdict


def flip_coin() -> dict:
    outcomes = defaultdict(int)
    total_cases = 10000

    for _ in range(total_cases):
        heads = 0
        for _ in range(10):  # 10 підкидань
            if random.choice(["H", "T"]) == "H":
                heads += 1
        outcomes[heads] += 1

    # перетворення в %
    return {
        k: round((v / total_cases) * 100, 2)
        for k, v in sorted(outcomes.items())
    }


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.bar(data.keys(), data.values(), color="skyblue")
    plt.xlabel("Number of Heads in 10 Tosses")
    plt.ylabel("Percentage (%)")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)
    plt.show()


data = flip_coin()
draw_gaussian_distribution_graph(data)
