import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_dict = {
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
    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(0, 1):
                count += 1
        for i in flip_dict:
            if count == i:
                flip_dict[i] += 1
    for count in flip_dict:
        flip_dict[count] /= 100
    return flip_dict


def draw_gaussian_distribution_graph() -> None:
    plt.plot(list(flip_coin().keys()), list(flip_coin().values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
