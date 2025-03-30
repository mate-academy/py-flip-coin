import random


def flip_coin() -> dict:
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    heads = 0
    for _ in range(10_000):
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1

        result.update({heads: result.get(heads) + 1})
        heads = 0

    for number, count in result.items():
        result.update({number: count / 10_000 * 100})

    return result
