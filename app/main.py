import random


def flip_coin() -> None:
    result_dict = {i: 0 for i in range(11)}
    for i in range(10000):
        head = 0
        for number in range(10):
            if random.choice(["Head", "beack"]) == "Head":
                head += 1
        result_dict[head] += 1

    for i in range(11):
        result_dict[i] /= 100
    return result_dict
