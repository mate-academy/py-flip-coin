import random


def flip_coin() -> dict:
    cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1

        results[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in results.items()
    }
