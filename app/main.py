import random


def flip_coin() -> dict[int, float]:
    cases = 10000

    results: dict[int, int] = {
        heads: 0
        for heads in range(11)
    }

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1

        results[heads] += 1

    percentages: dict[int, float] = {}

    for heads in results:
        percentages[heads] = round(
            results[heads] / cases * 100,
            2
        )

    return percentages
