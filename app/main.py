from random import choice


def flip_coins():
    dict_of_values = {}
    cases = [[choice((True, False)) for _ in range(10)] for _ in range(10000)]

    for case in cases:
        if case.count(True) in dict_of_values:
            dict_of_values[case.count(True)] += 1
        else:
            dict_of_values[case.count(True)] = 1

    dict_of_values = dict(sorted(dict_of_values.items()))

    return {key: value / 100 for key, value in dict_of_values.items()}
