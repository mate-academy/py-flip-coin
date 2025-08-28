import random


def flip_coin() -> dict:
    dictionary = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                  5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(0, 10000):
        count = 0
        for i in range(0, 10):
            result = random.randint(0, 1)
            if result == 1:
                count += 1
        dictionary[count] += 1 / 100
    return dictionary
