import random


def flip_coin():
    result_flipping = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            flip_result = random.randint(0, 1)
            if flip_result:
                heads += 1
        result_flipping[heads] += 1
    return {k: v / 100 for k, v in result_flipping.items()}
