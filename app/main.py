import random


def flip_coin():
    counting = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        counting[heads] += 1
    result = {key: value / 100 for key, value in counting.items()}
    return result
