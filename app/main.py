import random


def flip_coin() -> dict:
    not_result = {}
    result = {}
    count_of_dropped_num = 0
    for num_of_try in range(10000):
        for i in range(10):
            random_num = random.randint(1, 2)
            if random_num == 2:
                count_of_dropped_num += 1
        if count_of_dropped_num not in not_result:
            not_result[count_of_dropped_num] = 1
        else:
            not_result[count_of_dropped_num] += 1
        count_of_dropped_num = 0
    for i in range(len(not_result)):
        result[i] = not_result[i]
        result[i] = result[i] * 100 / 10000
    return result
