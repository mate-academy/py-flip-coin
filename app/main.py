import random


def flip_coin(num_cases: int = 10000,
              num_flips: int = 10
              ) -> dict:
    results = {}

    for _ in range(num_cases):
        num_heads = sum(random.choice((0, 1))
                        for _ in range(num_flips))
        results[num_heads] = -~results.get(num_heads, 0)

    return {times: percentage / num_cases * 100
            for times, percentage in results.items()}
