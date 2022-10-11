import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res = {i: 0 for i in range(11)}
    for _ in range(10000):
        flip = [random.randint(0, 1) for _ in range(10)]
        count_heads = flip.count(1)
        for key, value in res.items():
            if key == count_heads:
                res[key] += 1
    for key, value in res.items():
        res[key] = value / 100
    return res


def draw_gaussian_distribution_graph() -> None:
    res = flip_coin()
    dpi = 100
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    plt.axis([0, 10, 0, 100])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    axis_x = res.keys()
    axis_y = res.values()
    plt.plot(axis_x, axis_y)
    fig.savefig("fig.png")
    plt.show()


draw_gaussian_distribution_graph()
