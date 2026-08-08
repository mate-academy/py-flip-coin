import random


def flip_coin():
    dict_of_causes = {num: 0 for num in range(11)}
    for _ in range(10000):
        count_of_head = 0

        for _ in range(10):
            if random.randint(1, 2) == 1:
                count_of_head += 1

        dict_of_causes[count_of_head] += 1

    return {key: value / 100 for key, value in dict_of_causes.items()}
