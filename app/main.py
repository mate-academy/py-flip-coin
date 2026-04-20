import random


def flip_coin() -> dict:
    num_dict = {}

    for _ in range(10000):
        count_come_up = 0
        for __ in range(10):

            random_num = random.randint(0, 1)
            if random_num == 1:
                count_come_up += 1

        if count_come_up in num_dict:
            num_dict[count_come_up] += 1
        else:
            num_dict[count_come_up] = 1

    res_dict = {
        key: round((value / 10000) * 100, 2)
        for key, value in num_dict.items()
    }

    return res_dict
