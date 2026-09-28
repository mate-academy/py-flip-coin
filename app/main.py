import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    randoms = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }

    for _ in range(10000):
        number = 0

        for _ in range(10):
            new_number = random.randint(0, 1)
            if new_number == 1:
                number += 1
        randoms[number] += 1

    for key, value in randoms.items():
        randoms[key] = value / 10000 * 100
    return randoms


def draw_gaussian_distribution_graph(coins: dict) -> None:
    xit = coins.keys()
    jit = coins.values()
    plt.plot(xit, jit)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
