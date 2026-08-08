import random


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    results = {}
    for _ in range(num_cases):
        coin_flips = [random.choice(["H", "T"]) for _ in range(num_flips)]
        num_heads = coin_flips.count("H")

        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1

    total_cases = num_cases
    percentages = {key: (value / total_cases) * 100 for key, value
                   in results.items()}

    return percentages


result = flip_coin()
print(result)
