import random


def flip_coin() -> dict:
    result = {}
    for heads_number in range(11):
        counter = 0
        for _ in range(10000):
            attempt = [
                random.randint(0, 1) for _ in range(10)
            ]
            if attempt.count(0) == heads_number:
                counter += 1
        percentage = round(counter / 10000 * 100, 3)
        result[heads_number] = percentage

    return result
