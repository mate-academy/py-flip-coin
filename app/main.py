from random import choice


def flip_coin():
    result = {i: 0 for i in range(11)}
    sides = [0, 1]
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            choice_side = choice(sides)
            heads += choice_side
        result[heads] += 1
    for key_index in range(11):
        result[key_index] = result[key_index] / 100
    return result
