import random
from collections import defaultdict

def flip_coin() -> dict:
    results = defaultdict(int)
    total_simulations = 10000

    for _ in range(total_simulations):
        heads_count = 0
        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads_count += 1
        results[heads_count] += 1

    percentages = {}
    for heads, count in results.items():
        percentages[heads] = round((count / total_simulations) * 100, 2)

    return percentages
