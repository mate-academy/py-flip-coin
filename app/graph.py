import matplotlib.pyplot as plt
from app.main import flip_coin


def draw_gaussian_distribution_graph() -> None:
    xpoints = flip_coin().keys()
    ypoints = flip_coin().values()
    plt.plot(xpoints, ypoints)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop Percentage %")
    plt.axis([0, 10, 0, 100])
    plt.show()
