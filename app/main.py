from random import randint


def flip_coin() -> dict:
    return_dict = {}
    throwing_result = []
    heads_count = []
    for throw in range(10000):
        for _ in range(10):
            throwing_result.append(randint(0, 1))
        else:
            heads_count.append(throwing_result.count(1))
            throwing_result = []
    for values in range(0, 11):
        return_dict[values] = round((heads_count.count(values)
                                     / len(heads_count)) * 100, 2)

    return return_dict
