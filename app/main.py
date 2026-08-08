from random import randint


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        n_heads = sum(randint(0, 1) for i in range(10))
        result[n_heads] += 1

    return {
        i: result[i] / 100 for i in range(11)
    }
