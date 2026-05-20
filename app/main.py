from random import randint


def flip_coin() -> dict:
    result_dict =\
        {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    count = 0
    for _ in range(10000):
        result_dict[count] += 1
        count = 0
        for check in range(10):
            if randint(1, 2) == 1:
                count += 1
    for key, value in result_dict.items():
        result_dict[key] = value / 100
    return dict(sorted(result_dict.items()))
