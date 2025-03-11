import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, int]:
    result_dict = {
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
        heads_count = 0
        for _ in range(10):
            heads_count += random.randint(0, 1)
        result_dict[heads_count] += 1
    sum_heads = sum(result_dict.values())
    for key in result_dict.keys():
        result_dict[key] = round((result_dict[key] / sum_heads) * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    points_dict = flip_coin()
    x_points = points_dict.keys()
    y_points = points_dict.values()

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.ylim(0, 100)
    plt.plot(x_points, y_points)
    plt.show()
