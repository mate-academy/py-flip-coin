import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    new_dict = {}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        if heads not in new_dict:
            new_dict[heads] = 1
        else:
            new_dict[heads] += 1

    percentage_dict = {}

    for index, value in new_dict.items():
        new_value = ((value * 100) / 10000)
        percentage_dict[index] = round(new_value, 2)

    return dict(sorted(percentage_dict.items()))


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x = list(data.keys())  # noqa: VNE001
    y = list(data.values())  # noqa: VNE001

    plt.plot(x, y)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")

    plt.show()
