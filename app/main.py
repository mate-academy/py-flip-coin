import random

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


new_dict = {}


def flip_coin() -> dict:
    new_list = []
    for case in range(10000):
        coin_flip_heads = 0
        for flip in range(10):
            if random.choice(["Heads", "Tails"]) == "Heads":
                coin_flip_heads += 1
        new_list.append(coin_flip_heads)

    for num in range(11):
        new_dict[num] = new_list.count(num) / 100
    return new_dict


def draw_gaussian_distribution_graph(result_dict: dict) -> None:

    mpl.rcParams.update({"font.size": 10})

    fig, ax = plt.subplots()

    plt.axis([0, 10, 0, 100])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    x1 = []
    y1 = []

    for key in result_dict:
        x1 += [key]
        y1 += [result_dict[key]]

    ax.plot(x1, y1, color="blue", linestyle="solid")
    # Set the interval of major tick marks on the "x" axis:
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    # Set the interval of major tick marks on the "y" axis:
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    # Set the interval of minor tick marks on the "y" axis:
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

    fig.set_figwidth(12)
    fig.set_figheight(8)

    plt.show()
