import random


def flip_coin() -> dict:
    amount_of_simulation = 10000

    drop_rate = {}
    for i in range(11):
        drop_rate[i] = 0

    for _ in range(amount_of_simulation):
        heads_count = 0
        for _ in range(10):
            if random.choice([True, False]):
                heads_count += 1
        drop_rate[heads_count] += 1

    return {
        key: round(value / amount_of_simulation * 100, 3)
        for key, value in drop_rate.items()
    }
