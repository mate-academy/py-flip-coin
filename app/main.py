import random


def flip_coin() -> dict:
    num_cases = 10000
    results = {flip: 0 for flip in range(11)}

    for _ in range(num_cases):
        count_of_head = round(sum(random.randint(0, 1) for _ in range(10)))
        results[count_of_head] += 1

    res = {key: value / num_cases * 100 for key, value in results.items()}
    return res
