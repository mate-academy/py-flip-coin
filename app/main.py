import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    counts = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = 0
        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads += 1
        counts[heads] += 1

    return {k: counts[k] * 100 / trials for k in counts}


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_axis = list(result.keys())
    y_axis = list(result.values())

    plt.plot(x_axis, y_axis, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 35)
    plt.show()
