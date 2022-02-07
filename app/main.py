import random


def flip_coin():
    number_of_cases = 10_000
    number_of_flips = 10
    head = 1
    count_of_heads = []

    for case in range(number_of_cases):
        count_of_heads.append([random.randint(0, 1)
                               for flip in range(number_of_flips)].count(head))

    return {i: (count_of_heads.count(i) * 100)
            / number_of_cases for i in range(11)}
