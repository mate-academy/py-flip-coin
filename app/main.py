import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {amount: 0 for amount in range(11)}

    for i in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice(["head", "tail"]) == "head":
                heads += 1
        results[heads] += 1

    statistic = {amount: round((results[amount]
                                / 10000) * 100, 2) for amount in results}

    return statistic


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads = list(data.keys())
    percentage = list(data.values())

    plt.plot(heads, percentage)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Head counts")
    plt.ylabel("Drop percentage %")
    plt.show()


print(draw_gaussian_distribution_graph())
