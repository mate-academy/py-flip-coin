import random


def flip_coin() -> dict:
    cases_number = 20_000
    flips_number = 10
    heads_counts = {
        heads_number: 0 for heads_number in range(flips_number + 1)
    }

    for _ in range(cases_number):
        heads_number = sum(random.choices((0, 1), k=flips_number))
        heads_counts[heads_number] += 1

    return {
        heads_number: cases_count * 100 / cases_number
        for heads_number, cases_count in heads_counts.items()
    }
