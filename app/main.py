import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_count = {number: 0 for number in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1
        heads_count[heads] += 1
    heads_with_percentage = {}
    for heads, count in heads_count.items():
        heads_with_percentage[heads] = count / 10000 * 100
    return heads_with_percentage


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    x_value, y_value = results.keys(), results.values()
    plt.plot(x_value, y_value)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.xlim(0, 10)
    plt.xticks(range(0, 11, 1))
    plt.show()
