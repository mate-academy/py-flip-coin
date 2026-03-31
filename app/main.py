import random


def flip_coin() -> dict:
    some_list = {}
    for i in range(10000):
        count_of_heads = 0
        for _ in range(10):
            count_of_heads += random.randint(1, 2) == 1
        if count_of_heads not in some_list:
            some_list[count_of_heads] = 0
        some_list[count_of_heads] += 1
    return {count_of_heads: total / 10000 * 100
            for count_of_heads, total in some_list.items()}
