import random


def flip_coin() -> dict:

    result_dict = {}

    for i in range(10 + 1):

        arr_of_cases = []

        for case in range(10000):

            result_of_10_drops = 0

            for drop in range(10):

                result_of_10_drops += random.randint(0, 1)

            arr_of_cases.append(result_of_10_drops)

        percentage = (arr_of_cases.count(i) / 10000) * 100
        result_dict[i] = round(percentage, 2)

    return result_dict
