import random


def flip_coin() -> dict:
    total_cases = 10000
    tails_count_result = {count: 0 for count in range(11)}

    for _ in range(total_cases):
        case_of_flipping = [random.randint(0, 1) for _ in range(10)]
        tails_count = case_of_flipping.count(1)
        tails_count_result[tails_count] += 1

    tails_count_result_percent = {
        key: round(val / total_cases * 100, 2)
        for key, val in tails_count_result.items()
    }
    return tails_count_result_percent
