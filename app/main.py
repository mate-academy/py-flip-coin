import random
from collections import defaultdict


def flip_coin(trials: int = 10000) -> dict:
    results = defaultdict(int)

    for _ in range(trials):
        heads_count = (
            sum(1 for _ in range(10)
                if random.choice(["heads", "tails"]) == "heads"))
        results[heads_count] += 1

    percentages = {heads: (count / trials) * 100
                   for heads, count in results.items()}
    return dict(sorted(percentages.items()))


print(flip_coin())
