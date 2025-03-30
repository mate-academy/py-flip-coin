import random


def flip_coin() -> dict[int, float]:
    flip_data = [random.choices((0, 1), k=10).count(1) for _ in range(10_000)]
    statistic = {
        num: round((0.01 * flip_data.count(num)), 2) for num in range(11)
    }
    return statistic
