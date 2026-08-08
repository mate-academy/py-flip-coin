import random


def flip_coin() -> dict:
    cases = 10000
    counts = {index: 0 for index in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice([0, 1]) == 1:   # 1 = heads
                heads += 1

        counts[heads] += 1

    return {
        key: round(value / cases * 100, 2)
        for key, value in counts.items()
    }
