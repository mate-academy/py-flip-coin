import random


def flip_coin(num_experiments: int = 10000) -> dict:
    statistics = {i: 0 for i in range(11)}
    for _ in range(num_experiments):
        result = sum(random.choice([0, 1]) for _ in range(10))
        statistics[result] += 1
        print(statistics)

    percentages = {key: (value / num_experiments) * 100
                   for key, value in statistics.items()}

    return percentages


print(flip_coin())
