import random


def head_or_tail() -> int:
    total = 0
    coin = ["head", "tail"]
    for _ in range(10):
        if random.choice(coin) == "head":
            total += 1
    return total


def flip_coin() -> dict:
    head_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        num = head_or_tail()
        head_dict[num] += 1

    for key, value in head_dict.items():
        head_dict[key] = round(value / 10000 * 100, 2)

    return head_dict
