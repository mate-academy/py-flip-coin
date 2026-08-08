from random import choice


def flip_coin(
        trials: int = 10000,
        flips_per_trial: int = 10
) -> dict:
    dic = {i: 0 for i in range(0, flips_per_trial + 1)}
    for _ in range(trials):
        count_of_heads = sum(choice([1, 0]) for _ in range(flips_per_trial))
        dic[count_of_heads] += 1
    for key in dic:
        dic[key] = round(dic[key] / trials * 100, 2)
    return dic
