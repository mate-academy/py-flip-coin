import random


def flip_coin(cases: int = 10000) -> dict:

    result_list = [
        sum(random.randint(0, 1) for _ in range(10))
        for _ in range(cases)
    ]

    result_dict = {}

    for num in set(result_list):
        result_dict[num] = round(result_list.count(num) / cases * 100, 2)

    return result_dict
