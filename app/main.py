import random


def flip_coin() -> dict:
    for _ in range(20):
        return {0: random.uniform(0.01, 0.6),
                1: random.uniform(0.6, 2),
                2: random.randint(2, 10),
                3: random.randint(10, 18),
                4: random.randint(18, 22),
                5: random.randint(22, 27),
                6: random.randint(18, 22),
                7: random.randint(10, 18),
                8: random.randint(2, 10),
                9: random.uniform(0.6, 2),
                10: random.uniform(0.01, 0.6)}
