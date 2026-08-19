import random
from collections import Counter

def flip_coin(trials: int = 10000, flips: int = 10) -> dict[int, float]:
    results = []

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips))  # 1 = орёл, 0 = решка
        results.append(heads)

    counts = Counter(results)

    percentages = {k: round((v / trials) * 100, 2) for k, v in counts.items()}

    for i in range(flips + 1):
        percentages.setdefault(i, 0.0)

    return percentages
