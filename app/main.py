import random


def flip_coin() -> dict:
    number_of_iterations = 10000
    heads = []
    result = {}
    counts = {x: 0 for x in range(11)}
    for _ in range(number_of_iterations):
        save_integer = 0
        for i in range(10):
            flip = random.randint(1, 2)
            if flip == 1:
                save_integer += 1
        heads.append(save_integer)
    for integer in heads:
        counts[integer] += 1
    for count in counts.keys():
        result[count] = counts[count] / number_of_iterations * 100
    return result
