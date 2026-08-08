from random import choice


def flip_coin() -> dict:
    statistic = {}
    to_choice = ["head", "tail"]

    for _ in range(10000):
        res = [choice(to_choice) for _ in range(10)].count("head")
        if statistic.get(res):
            statistic[res] += 1
        else:
            statistic[res] = 1

    return {key: val / 100 for key, val in statistic.items()}
