
import random


def flip_coin() -> dict[int, float]:
    """Simulate flipping a coin 10 times in 10,000 cases."""
    cases = 10000
    flips_per_case = 10

    results = {number: 0 for number in range(11)}

    for _ in range(cases):
        heads = sum(
            random.choice([0, 1])
            for _ in range(flips_per_case)
        )

        results[heads] += 1

    percentages = {
        number: round((count / cases) * 100, 2)
        for number, count in results.items()
    }

    return percentages
