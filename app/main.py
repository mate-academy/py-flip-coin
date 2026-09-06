import math
import random


def flip_coin() -> dict:
    results = {}

    for i in range(11):
        results[i] = 0

    for case in range(10000):
        heads = 0

        for flip in range(10):
            result = random.randint(0, 1)

            if result == 1:
                heads += 1

        results[heads] += 1

    for heads in results:
        percent_count = results[heads] / 10000 * 100
        results[heads] = math.floor(percent_count * 100) / 100

    return results
