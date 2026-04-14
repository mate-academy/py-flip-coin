import random


def flip_coin(amount_of_cases: int = 10000) -> dict:
    result_dict = {i: 0.0 for i in range(11)}
    for _ in range(amount_of_cases):
        heads = sum(random.randint(0, 1) for _ in range(10))
        result_dict[heads] += 1

    for key in result_dict.keys():
        result_dict[key] = round(result_dict[key] / amount_of_cases * 100, 2)

    return result_dict
