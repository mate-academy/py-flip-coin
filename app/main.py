import random


def flip_coin() -> dict:
    numbers = {i: 0 for i in range(11)}
    for i in range(10000):
        heads = 0
        for flip in range(10):
            heads_or_tails = random.randint(0, 1)
            if heads_or_tails == 0:
                heads += 1
        numbers[heads] += 1
    for i in numbers.keys():
        numbers[i] = round(numbers[i] / 10000 * 100, 2)
    return numbers
