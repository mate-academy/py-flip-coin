import random


def flip_coin() -> dict[int, float]:
    num_simulations = 10000
    num_flips = 10
    counts = [0] * (num_flips + 1)
    for _ in range(num_simulations):
        heads_count = (
            sum(random.choice([0, 1]) for _ in range(num_flips))
        )
        counts[heads_count] += 1
    percentages = {
        i: (count / num_simulations)
        * 100 for i, count in enumerate(counts)
    }

    return percentages
