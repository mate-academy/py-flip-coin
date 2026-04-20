import random


def flip_coin() -> dict:
    data = {}
    for i in range(0, 11):
        data[i] = 0

    for flip in range(0, 10001):
        count_heads = 0
        for heads in range(0, 10):
            coin = random.randint(0, 1)
            if coin == 1:
                count_heads += 1
        data[count_heads] += 1
    for i in data:
        data[i] = (data[i] / 10000) * 100
    return data
