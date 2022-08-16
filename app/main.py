import random


def flip_coin():
    result = {}.fromkeys(range(11), 0)
    count_drops = 10000

    for i in range(count_drops):
        key = round(random.gauss(5, 1.6))
        if 0 <= key <= 10:
            result[key] += 1

    for key in result:
        result[key] = result[key] * 100 / 10000

    return result


print(flip_coin())
