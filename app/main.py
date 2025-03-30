import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    variants = ["heads", "tails"]

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            choice = random.choice(variants)
            if choice == "heads":
                heads_count += 1
        result_dict[heads_count] += 1
    for key in result_dict:
        result_dict[key] = (result_dict[key] / 10000) * 100
    return result_dict
