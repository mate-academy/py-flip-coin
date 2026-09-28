import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    heads_count = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(
            random.choice([0, 1]) for _ in range(10)
        )
        heads_count[heads] += 1

    return {
        heads: round((count / trials) * 100, 2)
        for heads, count in heads_count.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_coords = list(data.keys())
    y_coords = list(data.values())

    plt.figure()
    plt.plot(x_coords, y_coords)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()
