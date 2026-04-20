import random


def flip_coin() -> dict:
    sides = ["head", "tail"]
    result_dict = {i: float(0) for i in range(11)}
    for _ in range(10_000):
        count = 0
        for _ in range(10):
            value = random.choice(sides)
            if value == sides[0]:
                count += 1
        result_dict[count] += 1
    for i in range(11):
        result_dict[i] = round((result_dict[i] / 10_000) * 100, 2)
    return result_dict
