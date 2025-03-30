import random


def flip_coin() -> dict:
    flip_coin_result = {i: 0 for i in range(10)}

    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.choice(["Head", "Tail"]) == "Head":
                count += 1
        flip_coin_result[count] = flip_coin_result.get(count, 0) + 1

    for key, value in flip_coin_result.items():
        flip_coin_result[key] = value / 100

    return flip_coin_result
