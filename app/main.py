import random


def flip_coin():
    cases_of_flipping = 10000
    number_of_flips = 10
    results = {i: 0 for i in range(number_of_flips + 1)}

    for _ in range(cases_of_flipping):
        flips = {1: 0, 0: 0}
        for flip_index in range(number_of_flips):
            flips[random.randint(0, 1)] += 1
        results[flips[1]] += 1

    for key in results:
        results[key] = int((results[key] / cases_of_flipping) * 100)

    return results
