import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice((True, False)):
                heads += 1
        result[heads] = round(result[heads] + 0.01, 2)
    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(data.keys(), data.values())
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


if __name__ == "__main__":
    flip_coin()
    draw_gaussian_distribution_graph(flip_coin())
