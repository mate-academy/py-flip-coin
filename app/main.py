import random
import typing


def flip_coin() -> typing.Dict:
    quantity_of_heads = 0
    list_of_possibilities = [0] * 11
    final_dict = {}

    for _ in range(10000):
        for _ in range(10):
            if random.randint(0, 1) == 1:
                quantity_of_heads += 1
        list_of_possibilities[quantity_of_heads] += 1
        quantity_of_heads = 0

    for i in range(11):
        final_dict[i] = list_of_possibilities[i] / 100

    return final_dict
