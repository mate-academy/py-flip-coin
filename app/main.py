import random


def flip_coin():
    number_of_cases = 10_000
    number_of_flips = 10

    result = {i: 0 for i in range(number_of_flips + 1)}

    for _ in range(number_of_cases):
        current_result = {1: 0, 0: 0}
        for flip_index in range(number_of_flips):
            current_result[random.randint(0, 1)] += 1
        result[current_result[1]] += 1

    for key in result:
        result[key] = int(
            (result[key] / number_of_cases) * 100
        )

    return result
