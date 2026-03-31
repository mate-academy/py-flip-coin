import random


def flip_coin() -> dict:
    our_dict: dict = {
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
        10: 0}
    for raz in range(0, 10001):
        orel = 0
        for i in range(1, 11):
            if random.randint(0, 1) == 1:
                orel += 1
        our_dict[orel] += 1
    for raz in range(0, 11):
        our_dict[raz] = (our_dict[raz] / 10000) * 100

    return our_dict
