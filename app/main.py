import random


def flip_coin() -> dict:
    result_dict = {0: 0, 1: 0, 2: 0,
                   3: 0, 4: 0, 5: 0,
                   6: 0, 7: 0, 8: 0,
                   9: 0, 10: 0}
    for _ in range(10000):
        head = 0
        for _ in range(10):
            value = random.randint(1, 2)
            if value == 2:
                head += 1
        result_dict[head] += 1
    all_values = 0
    for i in range(10):
        all_values += result_dict[i]
    for key in result_dict:
        result_dict[key] = round((result_dict[key] / all_values) * 100, 2)
    return result_dict
