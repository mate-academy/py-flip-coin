import random
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker


def flip_coin() -> dict:
    result = {i: 0 for i in range(0, 11)}
    for _ in range(10000):
        head = 0
        for _ in range(10):
            head += random.randint(0, 1)

        result[head] += 1

    for key, value in result.items():
        result[key] = value / 100

    return result


# def draw_gaussian_distribution_graph(flips: dict) -> None:
#     dpi = 80
#     fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
#     mpl.rcParams.update({"font.size": 10})
#     ax = plt.axes()
#     ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
#     ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
#
#     plt.axis([0, 10, 0, 100])
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.plot(flips.keys(), flips.values(), color="blue", linestyle="solid",
#              label="Drops")
#     plt.legend(loc="upper right")
#     fig.savefig("gauss.png")
