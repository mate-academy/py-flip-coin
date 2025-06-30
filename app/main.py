import random


def flip_coin() -> dict:
    dict_of_head_percentage = {
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
        10: 0
    }
    for i in range(10001):
        head_percentage = 0
        for _ in range(10):
            coin = ["head", "tail"]
            flip = random.choice(coin)
            if flip == "head":
                head_percentage += 1
        dict_of_head_percentage[head_percentage] += 1
    for _ in range(11):
        dict_of_head_percentage[_] = (dict_of_head_percentage[_] / 10000) * 100
    return dict_of_head_percentage
