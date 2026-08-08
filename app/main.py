import random


def flip_coin() -> dict:
    result_dict = {key: 0 for key in range(11)}
    for _ in range(10000):
        number = sum(random.choice([0, 1]) for _ in range(10))
        result_dict[number] += 1
    percentages = {
        key: round((value / 100), 2) for key, value in result_dict.items()
    }
    return percentages
