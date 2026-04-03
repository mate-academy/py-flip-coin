import random


def flip_coin() -> dict:
    trials = 10000
    tosses_per_trial = 10
    counts = {heads: 0 for heads in range(tosses_per_trial + 1)}

    for _ in range(trials):
        heads = sum(random.randint(0, 1) for _ in range(tosses_per_trial))
        counts[heads] += 1

    return {
        heads: round((count / trials) * 100, 2)
        for heads, count in counts.items()
    }
