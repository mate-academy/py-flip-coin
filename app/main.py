import random


def flip_coin(num_trials : int = 10000) -> dict[int, float]:
    result = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        result[heads_count] += 1

    percentages = {
        key: round((value / num_trials) * 100, 2)
        for key, value in result.items()
    }
    return percentages
