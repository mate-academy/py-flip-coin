import random


def flip_coin() -> dict:
    heads_count = {i: 0 for i in range(11)}
    num_trials = 10000
    for _ in range(num_trials):
        flips = [random.choice([1, 0]) for _ in range(10)]
        num_heads = sum(1 for flip in flips if flip == 1)
        heads_count[num_heads] += 1
    heads_percent = {k: v / num_trials * 100 for k, v in heads_count.items()}
    heads_percent_rounded = {k: round(v, 2) for k, v in heads_percent.items()}
    return heads_percent_rounded
