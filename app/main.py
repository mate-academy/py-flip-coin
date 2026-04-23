import random
from collections import Counter


def flip_coin(num_flips: int = 10, num_trials: int = 10000) -> float:
    results = []

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results.append(heads_count)

    count_heads = Counter(results)
    total_cases = sum(count_heads.values())

    percentages = {
        heads: (count / total_cases) * 100 for heads,
        count in count_heads.items()
    }
    return percentages
