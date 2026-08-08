from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_dict = {key : 0 for key in range(11)}
    for _ in range(10000):
        heads = 0
        for i in range(10):
            heads += randint(0, 1)
        flip_dict[heads] += 1
    for key in flip_dict.keys():
        flip_dict[key] /= 100
    return flip_dict


def draw_gaussian_distribution_graph(flip_dict: dict) -> None:
    plt.plot(flip_dict.keys(), flip_dict.values())

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(11))
    plt.grid()

    plt.show()
