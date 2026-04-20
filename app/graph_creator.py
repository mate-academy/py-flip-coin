import matplotlib.pyplot as plt
from app.main import flip_coin


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    coord_x = list(data.keys())
    coord_y = list(data.values())

    plt.plot(coord_x, coord_y, linestyle="-")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
