import math
import random


def factorial(n: int):
    if n == 0:
        return 1
    else:
        return math.prod([a for a in range(1, n + 1)])


def flip_coin() -> dict:
    head = 0
    flip = 0
    result = {}
    for _ in range(0, 10_000):
        z = random.randint(0, 1)
        if z == 1:
            head += 1
        else:
            flip += 1

    head /= 10_000
    flip /= 10_000

    for one_flip in range(0, 11):
        y = factorial(10) / (factorial(one_flip) * factorial(10 - one_flip))
        x = y * (head ** one_flip) * (flip ** (10 - one_flip))
        result.update({one_flip: x * 100})
    return result
