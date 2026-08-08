import random

from matplotlib import pyplot as plt


def flip_coin() -> dict:
    coin_dict = {}
    total_experiments = 20000
    for _ in range(20000):
        total_heads = sum(random.choice([0, 1]) for _ in range(10))
        coin_dict[total_heads] = coin_dict.get(total_heads, 0) + 1
    for i in range(11):
        coin_dict[i] = coin_dict.get(i, 0)
    for elem in coin_dict:
        coin_dict[elem] = round(coin_dict[elem] / total_experiments * 100, 2)
    result = {k: coin_dict[k] for k in sorted(coin_dict)}
    return result


def draw_gaussian_distribution_graph() -> None:
    points = flip_coin()
    point_x = []
    point_y = []

    for elem in points:
        point_x.append(elem)
        point_y.append(points[elem])

    plt.plot(point_x, point_y)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drope percentage %")
    plt.show()
