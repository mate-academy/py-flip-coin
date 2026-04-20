import random


def flip_coin() -> dict:
    flips = 10000
    flip_dict = {i: 0 for i in range(11)}  # 0..10 орлів

    for _ in range(flips):
        heads = 0

        for _ in range(10):  # 10 підкидів монети
            random_flip = random.randint(1, 2)
            if random_flip == 1:
                heads += 1

        flip_dict[heads] += 1

    probabilities = {}

    for eagle in flip_dict:
        probabilities[eagle] = (flip_dict[eagle] / flips) * 100

    return probabilities


print(flip_coin())
