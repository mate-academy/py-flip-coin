import random


def flip_coin() -> dict:
    flip_data_set = [[random.randint(0, 1) for _ in range(10)]
                     for _ in range(10000)]
    data_set_analyzed = {key: len(
        [key_value_set for key_value_set in flip_data_set
         if sum(key_value_set) == key]
    ) / len(flip_data_set) * 100 for key in range(11)}

    return data_set_analyzed
