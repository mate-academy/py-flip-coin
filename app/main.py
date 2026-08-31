import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    heads = 0
    tails = 0
    for _ in range(10000):
        heads = 0
        tails = 0
        for _ in range(10):
            temp = random.randint(0, 1)
            if temp == 0:
                heads += 1
            else:
                tails += 1
        if heads not in result:
            result[heads] = 1
        else:
            result[heads] += 1
    return {
        key: (value / 10000 * 100)
        for key, value
        in sorted(result.items())
    }


def draw_gaussian_distribution_graph() -> None:
    random_dict = flip_coin()

    x_points = random_dict.keys()
    y_points = random_dict.values()

    plt.plot(x_points, y_points, marker="o")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid()
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.show()
