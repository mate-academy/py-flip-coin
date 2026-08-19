import random


def flip_coin() -> dict:
    dictionary = {item: 0 for item in range(11)}

    for item in range(10000):
        count = 0

        for jtem in range(10):
            if random.randint(0, 1):
                count += 1

        dictionary[count] += 1

    for key, value in dictionary.items():
        dictionary[key] = (value / 10000) * 100

    return dictionary
