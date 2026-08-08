import random


def flip_coin() -> dict:
    result_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                   6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    counter = 0
    for cases in range(10000):
        for flip in range(10):
            head = random.randint(0, 1)
            if head == 1:
                counter += 1
        result_dict[counter] += 1
        counter = 0

    result_dict_percent = {i: result_dict[i] / 100 for i in range(11)}
    return result_dict_percent
