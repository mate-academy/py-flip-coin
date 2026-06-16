import matplotlib.pyplot as plt
from main import flip_coin


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    x_values = list(distribution.keys())
    y_values = list(distribution.values())
    plt.plot(x_values, y_values)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.title("Gaussian distribution")
    plt.yticks(range(0, 101, 10))
    plt.show()
