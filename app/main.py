import random


def flip_coin() -> dict:
    result = {}
    count_heads = 0
    for i in range(10000):
        count_heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                count_heads += 1
        if count_heads in result.keys():
            result[count_heads] += 1
        else:
            result[count_heads] = 1
    for key, number in result.items():
        result[key] = (number * 100) / 10000

    return result
# write your code here
