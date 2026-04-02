import random


def get_heads_by_flips(size: int) -> int:
    heads = 0
    for _ in range(size):
        heads += random.choice([0, 1])
    return heads


def flip_coin() -> dict:
    times = 10000
    size = 10
    result_dict = {}
    for _ in range(times):
        key = get_heads_by_flips(size)
        if result_dict.get(key) is None:
            result_dict[key] = 0
        else:
            result_dict[key] += 1
    return {key: val / times * 100 for key, val in result_dict.items()}
