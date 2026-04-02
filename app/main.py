import random


def flip_coin(trials: int = 10000, flips_per_trial: int = 10) -> dict:
    outcomes = {num: 0 for num in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads_count = 0
        for _ in range(flips_per_trial):
            if random.random() < 0.5:
                heads_count += 1

        outcomes[heads_count] += 1

    for num in outcomes:
        outcomes[num] = (outcomes[num] / trials) * 100

    return outcomes
