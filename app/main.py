import random


def flip_coin() -> dict[int, float]:
    heads = {i: 0 for i in range(0, 11)}

    for i in range(10_000):
        count = 0

        for _ in range(10):
            if random.choice((1, 2)) == 1:
                count += 1

        heads[count] += 1

    for key, value in heads.items():
        heads[key] = round((value / 10_000) * 100, 2)

    return heads


flip_coin()
