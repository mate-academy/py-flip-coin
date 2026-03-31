from random import choice


def flip_coin() -> dict:
    result = {}
    for i in range(11):
        result[i] = 0
    cases = 10000
    for _ in range(cases):

        count = 0
        for _ in range(10):
            flip = choice([0, 1])
            if flip == 1:
                count += 1
        result[count] += 1

    return {index: (value * 100 / cases) for index, value in result.items()}
