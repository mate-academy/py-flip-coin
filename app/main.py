import random


def flip_coin() -> dict:
    new_dict = {}
    for num in range(11):
        new_dict[num] = 0
    for _ in range(10001):
        head_coin = 0
        for _ in range(10):
            number = random.randint(0, 1)
            if number == 0:
                head_coin += 1
        if head_coin in new_dict:
            new_dict[head_coin] += 1
    for elem in range(11):
        new_dict[elem] = new_dict[elem] * 100 / 10000
    return new_dict
