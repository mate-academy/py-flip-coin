import random


def flip_coin(number: int = 10000) -> dict:
    drop_options_lst = ["Eagle", "Tails"]
    dropout_results_lst = []
    for round_throws in range(number):
        count_eagle = 0
        for toss in range(10):
            if random.choice(drop_options_lst) == "Eagle":
                count_eagle += 1
        dropout_results_lst.append(count_eagle)
    return {
        x: dropout_results_lst.count(x) / number * 100 for x in range(0, 11)
    }
