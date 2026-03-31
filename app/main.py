from random import randint


def flip_coin() -> dict:
    res = {}
    num_of_cases = 10_000
    possible_heads = 10
    for _ in range(num_of_cases):
        head = 0
        for _ in range(possible_heads):
            head += randint(0, 1)
        if head in res.keys():
            res[head] += 1
        else:
            res.update({head: 1})
    return {k: res[k] * 100 / num_of_cases for k in sorted(res)}
