import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentage_results = {
        key: round((value / trials) * 100, 2)
        for key, value in results.items()
    }

    return percentage_results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    xx = list(data.keys())
    yy = list(data.values())

    plt.plot(xx, yy, color="blue")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))

    plt.show()

    print(flip_coin())


draw_gaussian_distribution_graph()
