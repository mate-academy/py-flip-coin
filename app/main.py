import random


def flip_coin() -> dict:
    random_flip = [
        sum(random.randint(0, 1) for _ in range(10)) for _ in range(5000)
    ]

    value = {num: round(random_flip.count(num) / len(random_flip) * 100, 3)
             for num in range(0, 11)}

    return value
