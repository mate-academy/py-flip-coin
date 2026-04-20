import random


def flip_coin() -> dict:
    num_flips = 10000
    heads_count = [0] * 11
    for _ in range(num_flips):
        num_heads = sum([random.choice([0, 1]) for i in range(10)])
        heads_count[num_heads] += 1

    result = {}
    for num_heads, count in enumerate(heads_count):
        result[num_heads] = round(count / num_flips * 100, 2)

    return result
