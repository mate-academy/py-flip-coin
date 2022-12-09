import matplotlib as mat
import matplotlib.pyplot as plot
import matplotlib.ticker as tick
from random import choice


def flip_coin() -> dict:
    result = []
    for _ in range(10000):
        eagle = 0
        for _ in range(10):
            if choice(["eagle", "tails"]) == "eagle":
                eagle += 1
        result.append(eagle)

    return {
        key: result.count(key) / 100
        for key in range(11)
    }


def draw_gaussian_distribution_graph(flip_coin_dict: dict) -> None:
    mat.rcParams.update({"font.size": 10})
    fig, ax = plot.subplots()
    plot.axis([0, 10, 0, 100])
    plot.title("Gaussian distribution")
    plot.xlabel("Heads count")
    plot.ylabel("Drop percentage %")
    x1 = []
    y1 = []

    for key in flip_coin_dict:
        x1 += [key]
        y1 += [flip_coin_dict[key]]

    ax.plot(x1, y1, color="blue", linestyle="solid")
    ax.xaxis.set_major_locator(tick.MultipleLocator(1))
    ax.yaxis.set_major_locator(tick.MultipleLocator(10))
    ax.yaxis.set_minor_locator(tick.MultipleLocator(5))
    fig.set_figwidth(12)
    fig.set_figheight(8)

    plot.show()


print(draw_gaussian_distribution_graph(flip_coin()))
