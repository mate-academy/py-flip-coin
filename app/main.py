import random


def flip_coin() -> dict:
    times = 10000
    coins_flipped = {x: 0 for x in range(11)}

    for _ in range(times):
        heads = 0

        for _ in range(10):
            heads += random.randint(0, 1)

        coins_flipped[heads] += 1

    result = {
        count: values / times * 100 for count, values in coins_flipped.items()
    }

    return result
