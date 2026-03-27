import random
import matplotlib.pyplot as plt

heads = 1


def flip_coin() -> dict:
    result = {}
    for _ in range(15000):
        heads_counter = 0

        for _ in range(1, 11):
            flip = random.randint(0, 1)
            if flip == heads:
                heads_counter += 1
        result[heads_counter] = result.get(heads_counter, 0) + 1

    for key, value in result.items():
        result[key] = (value / 15000) * 100

    return result

def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    xpoints = sorted(distribution.keys())
    ypoints = [distribution[key] for key in xpoints]

    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()