import random


def flip_coin() -> dict:
    nr_of_occurences = {i: 0 for i in range(11)}
    for _ in range(100000):
        nr_of_heads = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                nr_of_heads += 1

        nr_of_occurences[nr_of_heads] += 1

    probability_of_heads = {}
    for key, value in nr_of_occurences.items():
        probability = round((value / 100000) * 100, 2)
        probability_of_heads[key] = probability

    return probability_of_heads
