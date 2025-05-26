import random


def flip_coin() -> dict:
    result = {}
    head_or_tail = ["head", "tail"]
    for each_experiment in range(10000):
        count_heads = 0
        for each_toss in range(10):
            if random.choice(head_or_tail) == "head":
                count_heads += 1
        if count_heads not in result:
            result[count_heads] = 1
        else:
            result[count_heads] += 1
    for key, values in result.items():
        result[key] = (values / 10000) * 100
    return result
