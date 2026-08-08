import random


def flip_coin() -> dict:
    cases_to_count = {case: 0 for case in range(11)}
    cases_to_percentage = {case: 0 for case in range(11)}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            is_head = random.randint(0, 1)
            if is_head:
                heads_count += 1
        cases_to_count[heads_count] += 1

    for case in cases_to_percentage.keys():
        cases_to_percentage[case] = round(
            (cases_to_count[case] / 10000) * 100, 2
        )
    return cases_to_percentage
