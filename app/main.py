import random


def flip_coin() -> dict:
    result = {}
    luck = ["top", "bottom"]
    for i in range(11):
        result[i] = 0

    for _ in range(10000):
        tops_count = 0
        for _ in range(10):
            if random.choice(luck) == "top":
                tops_count += 1
        result[tops_count] += 1

    for key in result:
        result[key] = (result[key] * 100 / 10000)
    return result
