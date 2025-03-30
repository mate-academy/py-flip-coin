# write your code here
import random


def flip_coin() -> dict:
    dict_result = {}

    for case in range(10000):
        heads_count = 0

        for flip in range(10):
            flip_result = random.choice(["heads", "tails"])
            if flip_result == "heads":
                heads_count += 1

        dict_result[heads_count] = dict_result.get(heads_count, 0) + 1

    for key, value in dict_result.items():
        dict_result[key] = round(value / 10000 * 100, 2)

    return dict_result
