import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    chances = {0: 0,
               1: 0,
               2: 0,
               3: 0,
               4: 0,
               5: 0,
               6: 0,
               7: 0,
               8: 0,
               9: 0,
               10: 0}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            heads = random.randint(0, 1)
            if heads == 1:
                count += 1

        chances[count] += 1

    for key, value in chances.items():
        chances[key] = round((value / 10000 * 100), 2)

    return chances


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    plt.plot(flip_coin().keys(), flip_coin().values())
    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.show()


print(draw_gaussian_distribution_graph())
