from random import choice


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = sum(choice([0, 1]) for _ in range(10))
        result[heads] += 1
    return {keys: (values / 100) for keys, values in result.items()}
