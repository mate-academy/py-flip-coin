import random
from collections import Counter


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> dict:
    results = []
    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results.append(heads_count)

    count_heads = Counter(results)
    percentages = {k: (v / num_trials) * 100 for k, v in count_heads.items()}

    return percentages


print(flip_coin())
