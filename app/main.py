import random
from collections import defaultdict


def flip_coin(
        num_flips: int = 10,
        num_trials: int = 10000) -> dict[int, float]:
    results = defaultdict(int)
    for _ in range(num_trials):
        heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads] += 1

    total = sum(results.values())
    return {k: round(v / total * 100, 2) for k, v in sorted(results.items())}


def draw_ascii_distribution_graph(data: dict[int, float]) -> None:
    max_value = max(data.values())
    scale_factor = 50 / max_value

    print("\nDistribution of Heads in 10 Coin Flips:")
    print("-" * 60)
    for heads, percentage in data.items():
        bar_length = int(percentage * scale_factor)
        print(f"{heads: 2d} | {"#" * bar_length} {percentage: .2f}%")
    print("-" * 60)
