import random


def flip_coin() -> dict:
    result_flip_coin = {}
    for number_heads in range(11):
        result_head = 0
        for _ in range(10000):
            count = 0
            for _ in range(10):
                if random.randint(0, 1) == 1:
                    count += 1
            if number_heads == count:
                result_head += 1
        result_flip_coin[number_heads] = result_head / 10000 * 100
    return result_flip_coin
