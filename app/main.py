import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_trials = 10000
    results = {heads: 0 for heads in range(11)}

    for _ in range(total_trials):
        heads_count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads_count += 1
        results[heads_count] += 1

    return {
        heads: (count / total_trials) * 100
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xticks(range(11))
    plt.ylim(0, 100)

    plt.show()
