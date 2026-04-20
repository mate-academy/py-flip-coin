import random


def flip_coin(number_of_flipping: int = 10000, count: int = 10) -> dict:
    random_dict = {}
    for _ in range(number_of_flipping):
        heads = sum(random.choice([0, 1]) for _ in range(count))
        random_dict[heads] = (random_dict.get(heads, 0)
                              + 1 / number_of_flipping * 100)
    return random_dict
