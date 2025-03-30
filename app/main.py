from random import choice


def flip_coin() -> dict:
    result = {}
    number_of_cases = 10000
    for i in range(11):
        result[i] = 0

    for _ in range(number_of_cases):
        head_counts = sum(1 for _ in range(10) if choice([True, False]))
        result[head_counts] += 1

    for key, value in result.items():
        result[key] = (value / number_of_cases) * 100
    return result
