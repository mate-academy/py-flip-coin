import random
import matplotlib.pyplot as plt


def flip_coin() -> None:
    results = {i: 0 for i in range(11)}  # словник 0-10
    attempts = 10000

    for _ in range(attempts):
        heads = sum(random.randint(0, 1) for _ in range(10))
        results[heads] += 1

    # переведи в проценти
    return {k: round(v / attempts * 100, 2) for k, v in results.items()}


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.figure(figsize=(8, 5))

    plt.plot(
        x_values,
        y_values,
        marker="o",
        color="blue",
        linestyle="-",
        linewidth=2,
    )

    plt.title("Gaussian Distribution (Coin Flip Simulation)")
    plt.xlabel("Heads Count (0-10)")
    plt.ylabel("Percentage (%)")

    plt.xticks(range(0, 11))
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()


if __name__ == "__main__":
    result = flip_coin()
    print(result)
    draw_gaussian_distribution_graph(result)
