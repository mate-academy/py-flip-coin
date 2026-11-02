import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, int]:

    head_dict = {}

    for _ in range(0, 10000):
        count = 0
        for _ in range(0, 10):
            result = random.choice(["heads", "tails"])
            if result == "heads":
                count += 1
        if count not in head_dict:
            head_dict[count] = 1
        else :
            head_dict[count] += 1

    return {key: value / 100 for key, value in sorted(head_dict.items())}


def draw_gaussian_distribution_graph() -> None:

    coin_results = flip_coin()

    x_axis, y_axis = coin_results.keys(), coin_results.values()

    plt.plot(x_axis, y_axis)
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.title("Gaussian Distribution")

    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.show()
