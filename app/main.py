import random


def flip_coin() -> dict:
    return {
        number:
            [sum(random.randint(0, 1)
                 for i in range(10))
             for j in range(10000)].count(number) / 100
        for number in range(11)
    }
