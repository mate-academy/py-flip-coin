from random import choice


def flip_coin() -> dict:
    possibilities = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                     6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        count = 0
        for _ in range(10):

            flip = choice([0, 1])
            if flip == 1:
                count += 1

        possibilities[count] += 1

    for i in range(11):
        possibilities[i] = round((possibilities[i] / 10000) * 100, 2)
    return possibilities
