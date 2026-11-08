import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    coins = 10
    results = {i: 0 for i in range(coins + 1)}

    for _ in range(trials):
        heads = 0
        for _ in range(coins):
            heads += random.randint(0, 1)
        results[heads] += 1

    return {
        heads: round((count / trials) * 100, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x = list(data.keys())
    y = list(data.values())

    plt.plot(x, y)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
