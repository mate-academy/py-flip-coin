import random


def percentage(
        part: int | float,
        whole: int | float) -> float:
    return 100 * float(part) / float(whole)


def dict_to_precentage(my_dict: dict, whole_number: int | float) -> dict:
    for key, value in my_dict.items():
        my_dict[key] = percentage(value, whole_number)
    return my_dict


def flip_coin() -> dict:
    operation_number = 10_000
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for _ in range(operation_number):
        coin_flips = []
        for _ in range(10):
            coin_flips.append(random.randint(0, 1))
        result[coin_flips.count(1)] += 1

    dict_to_precentage(result, operation_number)
    return result
