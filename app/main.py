import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def flip_coin(num_of_cases):
    data = {num: 0 for num in range(11)}

    for _ in range(num_of_cases):
        flip = []
        for flips in range(10):
            flip.append(random.choice(["head", "tail"]))
        data[flip.count('head')] += 1

    data_percentage = {}
    for num, counts in data.items():
        data_percentage[num] = counts / (num_of_cases / 100)

    return draw_gaussian_distribution_graph(data_percentage)


def draw_gaussian_distribution_graph(data: dict):

    fig, ax = plt.subplots()

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.axis([0, 10, 0, 100])

    x_arr = []
    y_arr = []
    for x, y in data.items():
        x_arr.append(x)
        y_arr.append(y)

    plt.plot(x_arr, y_arr, 'b')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

    plt.show()
    return data


flip_coin(10000)
