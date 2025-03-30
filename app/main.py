from random import randint


def flip_coin() -> dict:
    number_of_coin = {}
    number_of_elements = 0
    while number_of_elements != 10000:
        result = [randint(0, 1) for i in range(0, 10, 1)].count(0)
        if result in number_of_coin.keys():
            number_of_coin[result] += 1
        else:
            number_of_coin[result] = 1
        result = 0
        number_of_elements += 1

    for key, value in number_of_coin.items():
        number_of_coin[key] = round((value / 10000) * 100, 2)
        sr_value = dict(sorted(number_of_coin.items(), key=lambda x: x[0]))
    return sr_value
