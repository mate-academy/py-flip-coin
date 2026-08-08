import random


def flip_coin(try_number: int = 10000, flip_coin: int = 10) -> None:
    dict_percent = {}
    for _ in range(try_number):
        prob_head = sum(random.choice([0, 1]) for _ in range(flip_coin))
        dict_percent[prob_head] = dict_percent.get(prob_head, 0) + 1
    result = {key: value / try_number * 100
              for key, value in dict_percent.items()}
    return result
