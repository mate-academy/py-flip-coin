import random


def flip_coin() -> dict:
    outcomes = {i: 0 for i in range(11)}
    num_trials = 10000

    for _ in range(num_trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        outcomes[heads] += 1

    outcomes_percentage = \
        {k: (v / num_trials) * 100 for k, v in outcomes.items()}
    return outcomes_percentage
