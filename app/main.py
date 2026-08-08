import random


def flip_coin() -> dict:
    final_dict = {}

    count_of_drops = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                      6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    sides = ["head", "another"]

    for _ in range(10000):
        count = 0
        for _ in range(10):
            drop = random.choice(sides)
            if drop == "head":
                count += 1
        count_of_drops[count] += 1

    for key in count_of_drops.keys():
        final_dict[key] = 100 * (count_of_drops[key] / 10000)

    return final_dict
