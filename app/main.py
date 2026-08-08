import random


def flip_coin(number: int = 10000) -> dict:

    drops = ["Eagle", "Tails"]
    dropout_result = []

    for round_throws in range(number):

        count_tails = 0

        for toss in range(10):
            if random.choice(drops) == "Tails":
                count_tails += 1
        dropout_result.append(count_tails)

    return {
        x: dropout_result.count(x) / number * 100 for x in range(0, 11)
    }
