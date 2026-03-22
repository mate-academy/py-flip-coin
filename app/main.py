import random
import matplotlib.pyplot as plt


def flip_coin():
    results = {i: 0.0 for i in range(11)}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1

        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / 10000 * 100, 2)

    return results


def draw_gaussian_distribution_graph():
    data = flip_coin()

    x = list(data.keys())
    y = list(data.values())

    plt.plot(x, y, marker='o')
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.ylim(0, 100)
    plt.grid()

    plt.show()


draw_gaussian_distribution_graph()
