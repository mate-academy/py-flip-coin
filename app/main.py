import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0.0 for i in range(11)}
    for _ in range(1, 10001):
        count = 0

        for flips in range(1, 11):
            flip = random.randint(0, 1)
            if flip == 1:
                count += 1

        result[count] += 1

    for numb in result:
        result[numb] = round(result[numb] / 10000 * 100, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_plot = list(data.keys())
    y_plot = list(data.values())

    plt.plot(x_plot, y_plot)
    plt.show()
