import random


def flip_coin() -> dict:
    flip_dict = {i: 0 for i in range(11)}
    for case in range(10000):
        count_of_heads = random.choices(["head", "tail"], k=10).count("head")
        flip_dict[count_of_heads] += 0.01
    return flip_dict
