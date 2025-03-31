import random


def flip_coin() -> dict:
    num_experiments = 10000
    heads = [sum(random.choice([0, 1]) for _ in range(10))
             for _ in range(num_experiments)]
    return {i: heads.count(i) / num_experiments * 100 for i in range(11)}
