import random
import matplotlib.pyplot as plt


def flip_coin():
    cases = 10000
    flips = 10

    counts = {i: 0 for i in range(flips + 1)}

    for _ in range(cases):
        heads = 0
        for _ in range(flips):
            if random.random() < 0.5:
                heads += 1
        counts[heads] += 1

    result = {}

    for k, v in counts.items():
        result[k] = round((v / cases) * 100, 2)

    return result


def draw_gaussian_distribution_graph(distribution):
    x = list(distribution.keys())
    y = list(distribution.values())

    plt.plot(x, y)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


if __name__ == "__main__":
    data = flip_coin()
    print(data)
    draw_gaussian_distribution_graph(data)
