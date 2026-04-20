import random
# import matplotlib.pylab as plt


def flipping() -> int:
    return sum(random.randint(0, 1) for _ in range(10))


def flip_coin() -> dict:

    distribution = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
        6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
    }
    for _ in range(10000):
        flip_result = flipping()
        distribution[flip_result] += 1

    for key, value in distribution.items():
        distribution[key] = distribution[key] / 100

    return distribution


# def draw_gaussian_distribution_graph(distribution: dict) -> None:
#     plt.axis([0, 10, 0, 100])
#     x, y = zip(*distribution.items())
#
#     plt.plot(x, y, color="blue", linestyle="solid",
#              label="")
#
#     plt.show()
