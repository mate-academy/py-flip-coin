import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict[int, float]:
    counts = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        counts[heads] += 1

    return {k: round(v * 100 / trials, 2) for k, v in counts.items()}


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    x = sorted(distribution.keys())
    y = [distribution[k] for k in x]

    plt.figure()
    plt.plot(x, y, linewidth=2)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.show()
