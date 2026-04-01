import random


def flip_coin() -> dict:
    result = {}
    coin_side = ["head", "tail"]

    for _ in range(10000):
        flips = []

        for _ in range(10):
            flips.append(random.choice(coin_side))

        for i in range(11):
            if flips.count("head") == i:
                if i in result.keys():
                    result[i] += 0.01
                    result[i] = round(result[i], 2)
                else:
                    result[i] = 0.01

    result_sorted = dict(sorted(result.items()))
    return result_sorted


print(flip_coin())
