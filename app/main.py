import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    trials = 10000

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        result[heads_count] += 1

    percentage_results = {key: (value / trials) * 100
                          for key, value in result.items()}
    return percentage_results
