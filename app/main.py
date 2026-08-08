import random
# from matplotlib import pyplot
# import numpy


def flip_coin() -> dict:
    coin = ["Head", "Tail"]
    result = {}
    drops_count = [0 for _ in range(11)]

    for _ in range(10000):
        flips = []
        for _ in range(10):
            flips.append(random.choice(coin))
        heads_count = flips.count("Head")
        drops_count[heads_count] += 1

    for count, drops in enumerate(drops_count):
        result[count] = (drops * 100) / 10000

    # x_points = [key for key in result.keys()]
    # y_points = [value for value in result.values()]
    # draw_gaussian_distribution_graph(x_points, y_points)

    return result


# def draw_gaussian_distribution_graph(x_points: dict, y_points: dict) -> None:
#     x_plot_points = numpy.array(x_points)
#     y_plot_points = numpy.array(y_points)

#     pyplot.plot(x_plot_points, y_plot_points)

#     pyplot.title("Gaussian distribution")
#     pyplot.xlabel("Heads count")
#     pyplot.ylabel("Drop percentage %")

#     pyplot.show()
