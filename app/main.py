import random


def flip_coin(cases_num: int = 10000, num_flips: int = 10) -> dict:
    heads_count = {head: 0 for head in range(num_flips + 1)}

    for _ in range(cases_num):
        flips = [random.choice(["heads", "tails"]) for _ in range(num_flips)]
        num_heads = flips.count("heads")
        heads_count[num_heads] += 1

    for heads in heads_count:
        heads_count[heads] = round((heads_count[heads] / cases_num) * 100, 2)

    return heads_count
