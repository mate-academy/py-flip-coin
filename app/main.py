import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count = {}
    for i in range(11):
        count[i] = 0
    for _ in range(10000):
        heads_count = 0
        for flip in range(10):
            result = random.randint(0, 1)
            if result == 1:
                heads_count += 1
        count[heads_count] += 1

    percentages = {}
    for key in count:
        percentages[key] = round((count[key] / 10000) * 100, 2)

    return percentages


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_axis = list(data.keys())
    y_axis = list(data.values())
    plt.bar(x_axis, y_axis)
    plt.show()
