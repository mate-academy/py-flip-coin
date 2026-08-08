import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    result = {}

    for number in range(11):
        result[number] = 0

    for _ in range(10000):
        heads = 0

        for _ in range(10):
            if random.choice([0, 1]) == 1:
                heads += 1

        result[heads] += 1

    for key in result:
        result[key] = round(result[key] / 10000 * 100, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads_counts = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads_counts, percentages)
    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.show()


draw_gaussian_distribution_graph()
