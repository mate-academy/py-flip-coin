from collections import defaultdict

import random


def flip_coin() -> dict:
    attempts = 10000
    coin = ["head", "tail"]
    dict_chance = defaultdict(int)

    for _ in range(attempts):
        number_of_heads_in_attempt = 0
        for num in range(10):
            result = random.choice(coin)
            if result == "head":
                number_of_heads_in_attempt += 1
        dict_chance[number_of_heads_in_attempt] += 1

    dict_chance = {
        heads_amount: (times_happened / attempts) * 100
        for heads_amount, times_happened in dict_chance.items()
    }

    return dict_chance
