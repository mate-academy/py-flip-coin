import random


def flip_coin():
    final = {i: 0 for i in range(11)}

    for _ in range(10000):
        num = 0
        for i in range(10):
            num += random.randint(0, 1)
        final[num] += 1

    for key in final.keys():
        final[key] = int(final[key] / 100)

    return final


print(flip_coin())
