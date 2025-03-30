import random


def flip_coin() -> dict:
    numbers = []
    for zero in range(11):
        numbers.append(0)
    for drops in range(10000):
        eagle = 0
        tails = 0
        for drop in range(10):
            rand = random.randint(0, 1)
            if rand == 0:
                tails += 1
            if rand == 1:
                eagle += 1
        for number in range(11):
            if number == tails:
                numbers[number] += 1
    dict_of_variants = {}
    for number in range(11):
        dict_of_variants[number] = numbers[number] / 100
    return dict_of_variants
