import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {
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
        10: 0
    }

    for i in range(10000):
        heads_count = 0
        for _ in range(10):
            heads_count += 1 if random.choice([0, 1]) else 0

        result[heads_count] += 1

    for i in range(11):
        result[i] = round(result[i] / 10000 * 100, 2)

    return result


# def draw_gaussian_distribution_graph(data: dict) -> None:
#     x_axscis = list(data.keys())
#     y_axscis = list(data.values())
#     ax = plt.gca()
#     ax.set_xlim([0, 10])
#     ax.set_ylim([0, 100])
#
#     plt.plot(x_axscis, y_axscis)
#
#     plt.suptitle("Gaussian distribution")
#     plt.ylabel("Drop percetage %Heads count")
#     plt.xlabel("Heads count")
#
#     plt.show()
