# import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    number_of_flips = 10000
    data = {i: 0 for i in range(11)}
    for _ in range(number_of_flips):
        count_1 = sum([1 for _ in range(10) if random.choice([0, 1]) == 1])
        data[count_1] += 1
    data = {
        key: round(value * 100 / number_of_flips, 2)
        for key, value in data.items()
    }
    return data


# def draw_gaussian_distribution_graph(data: dict) -> None:
#     xpoints = list(data.keys())
#     ypoints = list(data.values())
#
#     plt.plot(xpoints, ypoints, color="b")
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.xlim(0, 10)
#     plt.ylim(0, 100)
#     plt.show()
