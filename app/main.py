import random


def flip_coin() -> dict:
    n = 10000
    m = 10

    d = {i: 0 for i in range(m + 1)}
    for _ in range(n):
        head = 0
        for _ in range(m):
            num = random.randint(0, 1)
            head += num == 0
        d[head] += 1

    for i in range(m + 1):
        d[i] /= n // 100

    return d
