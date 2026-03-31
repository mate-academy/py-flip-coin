import random


def flip_coin() -> dict:
    new_dict = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for _ in range(10000):
        head = 0
        for num in range(0, 10):
            flip = random.random()
            if flip > 0.5:
                head += 1
        new_dict[head] += 1
    for key, value in new_dict.items():
        new_dict[key] = round(value / 10000 * 100, 2)

    return new_dict
