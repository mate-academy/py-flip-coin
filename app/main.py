from random import randint


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        count = 0
        for i in range(10):
            if randint(0, 1) == 1:
                count += 1
        result_dict[count] += 1

    for key, value in result_dict.items():
        result_dict[key] = value / 100

    return result_dict
