from random import randint


def flip_coin() -> dict[int, float]:
    result = {key: 0 for key in range(11)}
    for _ in range(10_000):
        counter = sum(randint(0, 1) == 1 for _ in range(10))
        result[counter] += 1
    for key in result:
        result[key] /= 100
    return result
