# import matplotlib.pyplot as plt

from random import randint


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        count_item = 0

        for _ in range(10):
            count_item += randint(0, 1)

        results[count_item] += 1

    return {
        key: (value / 10000 * 100)
        for key, value in results.items()
    }


# def draw_gaussian_distribution_graph(data: dict) -> None:
#     plt.plot(data.keys(), data.values())
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#
#     plt.show()
