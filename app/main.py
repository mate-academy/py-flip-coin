from random import choice


def flip_coin() -> None:
    result = dict.fromkeys(range(11), 0)
    iteration_number = 7000

    for i in range(iteration_number):
        streak = 0
        for _ in range(10):
            if choice((0, 1)):
                streak += 1
        result[streak] += 1

    for key, value in result.items():
        result[key] = round(value / iteration_number * 100, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt

    result = flip_coin()
    xpoints = result.keys()
    ypoints = result.values()

    plt.plot(xpoints, ypoints)
    plt.xlim(1, 10)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop persentage %")

    plt.show()
