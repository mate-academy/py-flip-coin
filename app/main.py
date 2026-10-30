from random import randint


def flip_coin() -> dict[int, float]:
    cases_count = 10000
    results = {heads: 0 for heads in range(11)}

    for _ in range(cases_count):
        heads_count = 0

        for _ in range(10):
            heads_count += randint(0, 1)

        results[heads_count] += 1

    return {
        heads: round(count * 100 / cases_count, 2)
        for heads, count in results.items()
    }# write your code here
