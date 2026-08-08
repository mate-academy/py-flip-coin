import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000, flips: int = 10) -> dict[int, float]:
    """Simulate coin flips and return distribution in percentages."""
    results: dict[int, int] = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        results[heads] += 1

    percentages: dict[int, float] = {
        k: round(results[k] / trials * 100, 2) for k in results
    }
    return percentages


def draw_gaussian_distribution_graph(results: dict[int, float]) -> None:
    """Draw Gaussian distribution graph using matplotlib."""
    x_values = list(results.keys())
    y_values = list(results.values())

    plt.plot(x_values, y_values, marker="o", color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    distribution = flip_coin()
    print(distribution)
    draw_gaussian_distribution_graph(distribution)
