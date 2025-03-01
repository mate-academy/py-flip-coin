import random


def flip_coin(times: int = 10000) -> dict:
    random_coin = {}

    for _ in range(times):
        value = sum([random.choice([0, 1]) for _ in range(10)])
        random_coin[value] = random_coin.get(value, 0) + 1

    random_coin = {k: round((v / times) * 100, 2)
                   for k, v in sorted(random_coin.items())}
    return random_coin
