import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    for i in range(10000):
        heads_counter = 0
        for _ in range(10):
            value = random.randint(0, 1)
            if value:
                heads_counter += 1
        result_dict[heads_counter] += 1

    return {key: value / 10000 * 100 for key, value in
            result_dict.items()}


print(flip_coin())


def draw_gaussian_distribution_graph(coin_flips: dict) -> None:
    xpoints = coin_flips.keys()
    ypoints = coin_flips.values()
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.plot(xpoints, ypoints)
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
