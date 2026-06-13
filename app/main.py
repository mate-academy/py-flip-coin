from random import choice


def flip_coin() -> dict:
    cases = {}

    for _ in range(10000):
        heads_count = sum(
            choice(["heads", "tails"]) == "heads" for _ in range(10)
        )
        cases[heads_count] = cases.get(heads_count, 0) + 1

    return {
        heads_count: round(
            count / 10000 * 100, 2) for heads_count, count in cases.items()
    }
