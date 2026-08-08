import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    counts = {k: 0 for k in range(11)}
    result_dict = {}
    total = 10000
    for _ in range(total):
        heads_count = 0
        for coin_flips in range(10):
            random_choice = random.choice(coin)
            if random_choice == "heads":
                heads_count += 1
        counts[heads_count] += 1

    for i in range(11):
        percentage = counts[i] / total * 100
        rounded_percentage = round(percentage, 2)
        result_dict[i] = rounded_percentage

    return result_dict
