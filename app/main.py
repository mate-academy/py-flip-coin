import random


def flip_coin(nums_of_flip: int = 10000, num_coins: int = 10) -> dict:
    result = {}

    for _ in range(nums_of_flip):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_coins))

        if num_heads in result:
            result[num_heads] += 1
        else:
            result[num_heads] = 1

    for key in result:
        result[key] = (result[key] / nums_of_flip * 100)

    return result
