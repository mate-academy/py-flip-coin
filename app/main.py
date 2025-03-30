import random
from collections import defaultdict


def flip_coin() -> None:
    trials = 10000
    flips_per_trial = 10
    heads_count = defaultdict(int)

    # Conduct trials
    for _ in range(trials):
        heads = sum(1 for _ in range(flips_per_trial)
                    if random.choice([0, 1]) == 1)
        heads_count[heads] += 1

    # Convert to percentages
    results = {heads: (count / trials) * 100 for
               heads, count in heads_count.items()}
    return results
