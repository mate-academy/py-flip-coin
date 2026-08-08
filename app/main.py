import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count = 0
    flip_dict = {}
    while count < 10001:
        head_count = 0
        for _ in range(1, 11):
            if random.randint(0, 1) == 1:
                head_count += 1
        flip_dict[head_count] = flip_dict.get(head_count, 0) + 1
        count += 1
    for key in flip_dict:
        flip_dict[key] = round(flip_dict[key] / 10001 * 100, 2)
    return flip_dict


def draw_gaussian_distribution_graph() -> None:
    points = flip_coin()
    plt.plot(points.keys(), points.values())
    plt.title("Gaussian_distribution")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.show()
