import random


def flip_coin():
    throw_count = []

    for _ in range(10000):
        round = 0

        for i in range(10):
            if random.randint(1, 2) == 1:
                round += 1
        throw_count.append(round)

    result = {x: (throw_count.count(x) / (len(throw_count) / 100))
              for x in range(11)}
    return result
