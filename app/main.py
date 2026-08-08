import random


def flip_coin() -> dict:
    flip_stats = {i: 0 for i in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        heads_count = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads_count += 1
        flip_stats[heads_count] += 1

    for key, value in flip_stats.items():
        flip_stats[key] = round((value / total_cases) * 100, 2)
    return flip_stats
