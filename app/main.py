import random


def flip_coin() -> dict:
    result_dict = {}
    coin_sides = ["heads", "tails"]
    for _ in range(1, 10001):
        heads = 0
        for _ in range(10):
            random_side = random.choice(coin_sides)
            if random_side == "heads":
                heads += 1
        if heads in result_dict:
            result_dict[heads] += 1
        else:
            result_dict[heads] = 1
    for number, quantity in result_dict.items():
        percentage = (quantity / 10000) * 100
        result_dict[number] = round(percentage, 2)
    sorted_result = dict(sorted(result_dict.items()))
    return sorted_result
