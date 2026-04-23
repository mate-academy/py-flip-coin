import random


def flip_coin() -> dict:
    check = ["heads", "tail"]
    result = dict.fromkeys(range(11), 0)
    for _ in range(10000):
        count = 0
        for i in range(10):
            if random.choice(check) == "heads":
                count += 1
        result[count] += 1
    for i in range(11):
        result[i] /= 100
    return result
