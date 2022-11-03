import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def flip_coin() -> dict:
    result_dict = {}
    for _ in range(10000):
        count = 0
        for i in range(10):
            x_side = random.randint(0, 1)
            if x_side == 1:
                count += 1
        if count in result_dict:
            result_dict[count] += 1
        else:
            result_dict[count] = 1
    keys = sorted(result_dict.items())
    sorted_dict = {}
    for key, value in keys:
        sorted_dict[key] = (value / 100)
    print(sorted_dict)
    return sorted_dict


def draw_gaussian_distribution_graph(data: dict) -> None:
    mpl.rcParams.update({"font.size": 10})
    plt.axis([0, 10, 0, 100])

    fig, ax = plt.subplots()
    x_axis = data.keys()
    y_axis = data.values()
    plt.plot(x_axis, y_axis, color="blue", linestyle="solid")

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(5))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    fig.savefig("Gaussian_distribution.png")
