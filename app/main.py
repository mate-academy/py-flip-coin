import random


def flip_coin() -> dict:
    randoms = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    for i in range(10000):
        head = 0
        for choice in range(0, 10):
            rand_choice = random.choice(["head", "bottom"])
            if rand_choice == "head":
                head += 1
        randoms[head] += 1

    for res in randoms:
        result = randoms[res] / 10000 * 100
        randoms[res] = result

    return randoms


if __name__ == "__main__":
    flip_coin()
