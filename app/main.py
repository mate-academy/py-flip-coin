import random


def flip_coin(n_series: int = 10000) -> dict:  # <- добавь типы
    counts = {i: 0 for i in range(11)}  # <- пробел после :
    for _ in range(n_series):
        heads = 0
        for _ in range(10):
            heads += random.choice([0, 1])
        counts[heads] += 1
    for k in counts:
        counts[k] = round(counts[k] / n_series * 100, 2)
    return counts
