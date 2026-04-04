import random


def flip_coin() -> dict:
    result_dict = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }

    for _ in range(10000):
        head = 0

        for _ in range(10):
            result = random.randint(0, 1)

            if result == 0:
                head += 1

        if head == 0:
            result_dict[0] += 1 / 10000 * 100
        if head == 1:
            result_dict[1] += 1 / 10000 * 100
        if head == 2:
            result_dict[2] += 1 / 10000 * 100
        if head == 3:
            result_dict[3] += 1 / 10000 * 100
        if head == 4:
            result_dict[4] += 1 / 10000 * 100
        if head == 5:
            result_dict[5] += 1 / 10000 * 100
        if head == 6:
            result_dict[6] += 1 / 10000 * 100
        if head == 7:
            result_dict[7] += 1 / 10000 * 100
        if head == 8:
            result_dict[8] += 1 / 10000 * 100
        if head == 9:
            result_dict[9] += 1 / 10000 * 100
        if head == 10:
            result_dict[10] += 1 / 10000 * 100
    return result_dict
