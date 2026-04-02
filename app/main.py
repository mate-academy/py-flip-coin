import random
from collections import Counter


def flip_coin(num_experiments: int = 10000) -> dict:
    results = [sum(random.choice([0, 1])
                   for _ in range(10)) for _ in range(num_experiments)]
    frequency = dict(Counter(results))
    total_experiments = sum(frequency.values())
    probability_distribution = {
        k: round(v / total_experiments * 100, 2) for k, v in frequency.items()
    }
    return probability_distribution
