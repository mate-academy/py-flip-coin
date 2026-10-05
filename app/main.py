import random


def flip_coin() -> dict:
    results = {}
    total_experiments = 10000
    experiment_count = 0

    for heads_count in range(11):
        results[heads_count] = 0

    while experiment_count < total_experiments:
        heads = 0

        for _ in range(10):
            result = random.randint(0, 1)

            if result == 1:
                heads += 1

        results[heads] = results[heads] + 1
        experiment_count += 1

    for heads_count in range(11):
        results[heads_count] = round(
            results[heads_count] / total_experiments * 100, 2
        )

    return results
