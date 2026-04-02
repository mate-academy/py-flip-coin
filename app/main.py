import random


def flip_coin() -> dict:
    final_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        count = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 0:
                count += 1
        final_dict[count] += 1

    for i in final_dict:
        final_dict[i] = round(final_dict[i] / 10000 * 100, 2)

    return final_dict
