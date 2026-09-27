import random


def flip_coin() -> dict[int, float]:
    number_of_cases = 10000
    results = {number: 0 for number in range(11)}

    for _ in range(number_of_cases):
        heads = 0

        for _ in range(10):
            heads += random.randint(0, 1)

        results[heads] += 1

    return {
        number: round(count / number_of_cases * 100, 2)
        for number, count in results.items()
    }
