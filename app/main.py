from random import choice


def flip_coin(flip: int = 10000) -> dict:
    statistics_throws = {i: 0 for i in range(11)}
    for _ in range(flip):
        count_eagle = 0
        for _ in range(10):
            if choice(["eagle", "tail"]) == "eagle":
                count_eagle += 1
        statistics_throws[count_eagle] += 1
    for key in statistics_throws:
        statistics_throws[key] = (statistics_throws[key] / flip) * 100
    return statistics_throws
