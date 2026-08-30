import random


def flip_coin() -> dict:
    all_flip_cases = [
        sum(random.randint(0, 1)
            for _ in range(10)) for _ in range(10000)
    ]
    return {
        x: all_flip_cases.count(x) / len(all_flip_cases) * 100
        for x in range(11)
    }
