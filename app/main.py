import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    trials = 10000
    flips_per_trial = 10
    results = {i: 0 for i in range(flips_per_trial + 1)}
    for _ in range(trials):
        heads_count = 0
        for _ in range(flips_per_trial):
            if random.random() < 0.5:
                heads_count += 1

        results[heads_count] += 1

    return {k: (v / trials) * 100 for k, v in results.items()}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_values = list(data.keys())
    y_values = list(data.values())

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, marker="o", linestyle="-", color="b")

    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage, %")
    plt.xticks(range(11))  # щоб на осі X були всі числа від 0 до 10
    plt.grid(True, alpha=0.3)

    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
