import random


def flip_coin() -> dict:
    num_cases = 10000
    num_flips = 10
    results = {heads: 0 for heads in range(num_flips + 1)}

    for case in range(num_cases):
        num_heads = sum([random.randint(0, 1) for _ in range(num_flips)])
        results[num_heads] += 1

    return {heads: occurrences / num_cases * 100
            for heads, occurrences in results.items()}
