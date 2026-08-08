import random


def flip_coin() -> dict:
    total_res = dict()

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.random() > 0.5:
                heads_count += 1
        if heads_count in total_res:
            total_res[heads_count] += 1
        else:
            total_res[heads_count] = 1

    total_heads_count = sum(total_res.values())
    percentage_res = dict()

    for key, value in total_res.items():
        percentage_res[key] = round((value / total_heads_count) * 100, 2)

    return percentage_res


print(flip_coin())
