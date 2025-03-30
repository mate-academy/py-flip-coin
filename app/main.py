import random
import matplotlib.pyplot as pl
from matplotlib.ticker import MultipleLocator


def flip_coin():
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        result[sum([random.randint(0, 1) for _ in range(10)])] += 1
    return {key: (value / 100) for key, value in result.items()}


def draw_gaussian_distribution_graph():
    data = flip_coin()
    x = list(data.keys())
    y = list(data.values())
    fig, ax = pl.subplots()
    pl.plot(x, y, color="b")
    pl.xlabel("Heads count", fontsize=10)
    pl.ylabel("Drop percentage %", fontsize=10)
    pl.title("Gaussian distribution")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    pl.axis([0, 10, 0, 100])
    pl.xticks(range(11))
    pl.yticks(range(0, 101, 10))
    pl.show()
