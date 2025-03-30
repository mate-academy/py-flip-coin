import random


def flip_coin() -> None:
    try_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }

    for rnd in range(10000):
        count_heads = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                count_heads += 1
        try_dict[count_heads] += 1

    percentages = {key: (value / 10000) * 100
                   for key, value in try_dict.items()}
    return percentages
