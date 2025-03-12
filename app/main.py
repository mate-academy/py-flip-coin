import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count_head = []
    result_dict = {}
    for i in range(10000):
        head_count_list = [random.choice([0, 1]) for _ in range(10)]
        count_head.append(sum(head_count_list))

    for i in range(11):
        result_dict[i] = round(count_head.count(i) / 10000 * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_points = list(result.keys())
    y_points = list(result.values())
    plt.plot(x_points, y_points)
    plt.show()
