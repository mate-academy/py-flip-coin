import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dic = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            flip = random.choice([0, 1])
            if flip == 1:
                heads += 1
        dic[heads] += 1

    for key, value in dic.items():
        dic[key] = round((value / 10000) * 100, 2)

    return dic


def draw_gaussian_distribution_graph() -> None:
    res = flip_coin()
    x_coord = list(res.keys())
    y_coord = list(res.values())

    plt.plot(x_coord, y_coord)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")

    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()
