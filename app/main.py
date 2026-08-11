import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counts = {i: 0 for i in range(11)}
    num_trials = 10000

    for _ in range(num_trials):
        flips = [random.randint(0, 1) for _ in range(10)]
        heads_count = sum(flips)

        counts[heads_count] += 1

    percentages = {}
    for heads, count in counts.items():
        percentages[heads] = count / num_trials * 100

    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_values = list(data.keys())
    y_values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, color="blue", linewidth=3)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian Distribution")
    plt.xticks(x_values)
    plt.ylim(0, 100)
    plt.show()
