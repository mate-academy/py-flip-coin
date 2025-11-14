import matplotlib.pyplot as plt

from main import flip_coin


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    plt.plot(distribution.keys(), distribution.values())

    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
