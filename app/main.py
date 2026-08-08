import random


def flip_coin() -> dict:
    result = {}
    all_cases = {}
    for i in range(0, 10000):
        counter = 0
        for _ in range(0, 10):
            coin = random.randint(1, 2)  # 1 = heads
            if coin == 1:
                counter += 1

        if counter in all_cases.keys():
            all_cases[counter] += 1
        else:
            all_cases[counter] = 1

    sum_all = sum(all_cases.values())

    for key, value in all_cases.items():
        result[key] = round(100 * value / sum_all, 2)

    return result
