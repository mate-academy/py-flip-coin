import random


def flip_coin() -> dict:
    stats_dict = {}
    for _ in range(10000):
        heads = 0
        tails = 0
        for toss in range(10):
            toss_value = random.choice(["heads", "tails"])
            if toss_value == "heads":
                heads += 1
            else:
                tails += 1
        stats_dict[heads] = stats_dict.get(heads, 0) + 1
    for key, value in stats_dict.items():
        stats_dict[key] = round(value * 100 / 10000, 2)
    return dict(sorted(stats_dict.items()))
