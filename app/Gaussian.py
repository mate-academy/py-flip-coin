import matplotlib.pyplot as plt


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x = list(data.keys())
    y = list(data.values())

    plt.plot(x, y)
    plt.xlabel("Number of Heads (out of 10)")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Flip Distribution (10 flips)")
    plt.show()
