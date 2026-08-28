import random


def flip_coin(
    trials: int = 10000, flips_per_trial: int = 10
) -> dict[int, float]:
    results_count = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads = sum(random.randint(0, 1) for _ in range(flips_per_trial))
        results_count[heads] += 1

    return {
        heads: round((count / trials) * 100, 2)
        for heads, count in results_count.items()
    }


print(flip_coin())
