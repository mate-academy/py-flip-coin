import random


def flip_coin() -> dict:
    flips = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        flips[heads] += 1

    for heads in flips:
        flips[heads] = round((flips[heads] / 10000) * 100, 2)

    return flips


def draw_gaussian_distribution_graph(flips: dict) -> None:
    import matplotlib.pyplot as plt

    x_vals = list(flips.keys())
    y_vals = list(flips.values())

    plt.plot(x_vals, y_vals)
    plt.xlabel("Heads Count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))

    plt.show()
