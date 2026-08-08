import random


def flip_coin() -> dict:
    dic = dict.fromkeys(range(11), 0)
    total_trials = 10000

    for _ in range(total_trials):
        heads_count = sum(random.randint(1, 2) == 1 for _ in range(10))
        dic[heads_count] += 1

    for key in dic:
        dic[key] = round((dic[key] / total_trials) * 100, 2)

    return dic
