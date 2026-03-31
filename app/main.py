import random
from collections import Counter


def flip_coin() -> dict:
    total_results = []
    trials = 10000
    count = 0
    while count != trials:
        result_10_times = []
        for i in range(10):
            res = random.choice(["heads", "tails"])
            result_10_times.append(res)
        heads_count = result_10_times.count("heads")
        total_results.append(heads_count)
        count += 1
    counts = Counter(total_results)
    percentages = {k: (v / trials) * 100 for k, v in counts.items()}
    return dict(sorted(percentages.items()))
