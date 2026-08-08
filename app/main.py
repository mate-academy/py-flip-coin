import random


def flip_coin() -> dict:
    result_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    for times in range(10000):
        times = 0
        for flip in range(10):
            head = random.randint(0, 1)
            if head == 1:
                times += 1

        result_dict[times] += 1

    for key, value in result_dict.items():
        result_dict[key] = round(value / 100, 3)
    return result_dict


print(flip_coin())
