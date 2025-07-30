import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from typing import Dict, List


def flip_coin(num_flips: int = 10, num_cases: int = 10000) -> Dict[int, float]:
    results: List[int] = []
    for _ in range(num_cases):
        flips: np.ndarray = np.random.randint(0, 2, num_flips)
        num_heads: int = np.sum(flips)
        results.append(num_heads)

    counts: Counter[int] = Counter(results)
    percentages: Dict[int, float] = {
        k: round((v / num_cases) * 100, 2) 
        for k, v in sorted(counts.items())
    }
    return percentages


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    head_counts: List[int] = list(distribution.keys())
    percentages: List[float] = list(distribution.values())

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=head_counts, y=percentages, palette="viridis")
    plt.title(
        "Distribution of Number of Heads in 10 Coin Flips (10,000 Cases)",
        fontsize=14
    )
    plt.xlabel("Number of Heads", fontsize=12)
    plt.ylabel("Percentage of Cases (%)", fontsize=12)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    result: Dict[int, float] = flip_coin()
    print(result)
    draw_gaussian_distribution_graph(result)
