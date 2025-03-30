import random


def flip_coin() -> dict:
    counter = 0
    dictionary = {i: 0 for i in range(11)}
    for jimi in range(10000):
        for i in range(10):
            flip = random.choice(["eagle", "tails"])
            if flip == "eagle":
                counter += 1
        for key in dictionary:
            if key == counter:
                dictionary[key] += 1
                counter = 0
    return {key: (value / 10000) * 100 for key, value in dictionary.items()}
