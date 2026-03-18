from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    new_dict = {}
    for coin in range(10000):
        eagle = 0
        for n in range(10):
            flip = randint(0, 1)
            if flip == 1:
                eagle += 1
        if eagle not in new_dict:
            new_dict[eagle] = 1
        else:
            new_dict[eagle] += 1
    final_dict = {}
    for i in range(11):
        count = new_dict.get(i, 0)
        final_dict[i] = count / 100
    return final_dict


def draw_gaussian_distribution_graph():
    data = flip_coin()
    x = list(data.keys())
    y = list(data.values())
    plt.plot(x, y, color="blue", marker="D")
    plt.show()
