import random


def flip_coin(trials: int = 10000) -> dict:
    dict_coin = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        dict_coin[heads] += 1
    result_dict = {heads: round(count / trials * 100, 2)
                   for heads, count in dict_coin.items()}
    return result_dict
