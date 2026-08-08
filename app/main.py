import random


def flip_coin() -> dict:
    flip_dict = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for i in range(15000):
        coin = 0
        for flip in range(10):
            coin += random.randint(0, 1)
        flip_dict[coin] = flip_dict[coin] + 1 / 150
    flip_dict = {num: round(prob, 2) for num, prob in flip_dict.items()}
    return flip_dict
