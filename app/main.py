import random


def flip_coin():
    result = {number: 0 for number in range(11)}
    for _ in range(10000):
        flips = ['Heads' if flip == 1 else 'Tails' for flip in
                 [random.randint(0, 1) for _ in range(10)]]
        heads = flips.count('Heads')
        result[heads] += 1
    for number, times in result.items():
        result[number] = round(times / 100, 2)
    return result
