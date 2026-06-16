import random


def flip_coin() -> dict:
    number_of_cases = 10000
    result = {i: 0 for i in range(11)}
    coin_sides = ["head", "tail"]
    number_of_heads = 0

    for case in range(number_of_cases):
        for throw in range(10):
            if random.choice(coin_sides) == "head":
                number_of_heads += 1
        result[number_of_heads] += 1
        number_of_heads = 0

    for i in range(0, 11):
        result[i] = result[i] * 100 / number_of_cases

    return result
