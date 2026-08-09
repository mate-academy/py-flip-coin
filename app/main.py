import random


def flip_coin() -> dict:
    percentage_dict = {x: 0 for x in range(0, 11)}
    for _ in range(1, 10001):
        ten_flip_results = []
        for _ in range(1, 11):
            ten_flip_results.append(random.randint(0, 1))
        heads_count = ten_flip_results.count(1)
        percentage_dict[heads_count] += 1

    for key in percentage_dict:
        percentage_dict[key] = round(percentage_dict[key] / 10000 * 100, 2)

    return percentage_dict
