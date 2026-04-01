import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    def flip() -> int:
        count = 0
        for _ in range(10):
            coin_side = random.randint(0, 1)
            if coin_side == 1:
                count += 1
        return count

    for _ in range(100000):
        result[flip()] += 1

    total_simulations = 100000
    result = {
        key: (value / total_simulations) * 100 for key,
        value in result.items()
    }

    return result
