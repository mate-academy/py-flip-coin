import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dict_coin = {key: 0.0 for key in range(11)}
    for _ in range(10000):
        throws = [random.randint(0, 1) for _ in range(10)]
        heads_count = sum(throws)
        dict_coin[heads_count] += 1

    for key in dict_coin:
        dict_coin[key] = round((dict_coin[key] / 10000) * 100, 2)

    return dict_coin


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_coords = list(data.keys())
    y_coords = list(data.values())
    plt.plot(x_coords, y_coords)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
