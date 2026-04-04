import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    cases = 20000
    counts = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(10))
        counts[heads] += 1

    return {heads: round(count / cases * 100, 2)
            for heads, count in counts.items()}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    names = list(data.keys())
    values = list(data.values())
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.plot(names, values)
    plt.show()
