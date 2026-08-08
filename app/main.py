import random


def flip_coin() -> dict:
    cases = ["heads", "tails"]
    times = 10000

    statistics = {}

    for key in range(10 + 1):
        statistics[key] = 0

    for _ in range(times):
        heads_results = []
        for _ in range(10):
            result = random.choice(cases)

            if result == "heads":
                heads_results.append("heads")

        statistics[len(heads_results)] += 1

    all_values = 0
    for value in statistics.values():
        all_values += value

    percent = all_values / 100

    for key, value in statistics.items():
        statistics[key] = value * percent / times

    return statistics
