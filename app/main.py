import random


def flip_coin():
    experiments = 100000
    result = {i: 0 for i in range(11)}

    for _ in range(experiments):
        heads = 0

        for _ in range(10):
            if random.choice([0, 1]) == 1:
                heads += 1

        result[heads] += 1

    for key in result:
        result[key] = round(result[key] / experiments * 100, 2)

    return result
