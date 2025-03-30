import random


def flip_coin() -> dict:
    results = {number: 0 for number in range(0, 11)}
    sides = ["heads", "tails"]
    for i in range(0, 10000):
        res_list = [random.choice(sides) for _ in range(0, 10)]
        new_value = res_list.count("heads")
        results[new_value] += 1
    finals = {
        key: round((value / 10000) * 100, 2) for key, value in results.items()
    }
    return finals
