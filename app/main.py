import random


def flip_coin() -> dict:
    result_dict = {}
    result_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for ten_coin_tosses in range(10000):
        heads_count = 0
        for coin_toss in range(10):
            coin_result = random.choice([True, False])
            if coin_result is True:
                heads_count += 1
        result_list[heads_count] += 1
    for index, value in enumerate(result_list):
        result_dict[index] = round(value / 100, 2)
    return result_dict
