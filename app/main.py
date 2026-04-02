import random


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
              5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        exact_key = sum(random.choice(["head", "tail"]) == "head"
                        for _ in range(10))
        result[exact_key] += 1
    for key, value in result.items():
        result[key] = value / 100
    return result
