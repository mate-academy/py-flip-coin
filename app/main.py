import random


def choice_side() -> dict:
    chance_head_dict = {}
    for _ in range(10000):
        count = count_head()
        if count not in chance_head_dict.keys():
            chance_head_dict[count] = 1
        else:
            chance_head_dict[count] += 1

    for number in chance_head_dict.keys():
        chance_head_dict[number] = round(chance_head_dict[number]
                                         / 10000 * 100, 2)

    return dict(sorted(chance_head_dict.items()))


def flip_coin() -> str:
    coin = ("head", "tail")
    return random.choice(coin)


def count_head() -> int:
    count = 0
    for _ in range(10):
        if flip_coin() == "head":
            count += 1

    return count
