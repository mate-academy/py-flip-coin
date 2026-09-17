import random
import matplotlib.pyplot as plt


def flip_coin(num_trials=10000, num_flips=10):
    counts = {k: 0 for k in range(num_flips + 1)}
    for _ in range(num_trials):
        heands = 0
        for _ in range(num_flips):
            if random.randint(0, 1) == 1:
                heands += 1
        counts[heands] += 1

    percentages = {
        k: round(count / num_trials * 100, 2)
        for k, count in counts.items()
    }
    return percentages


def draw_graph(data):
    x = list(data.keys())
    y = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color="skyblue", edgecolor="black")
    plt.title("Gaussian Distribution")
    plt.xlabel("Drop percentages, %")
    plt.ylabel("Heands count")

    plt.xticks(x)
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    for xi, yi in zip(x, y):
        plt.text(xi, yi + 0.3, str(yi), ha="center", fontsize=9)

    plt.show()

    if __name__ == "__main__":
        result = flip_coin()
        print(result)
        draw_graph(result)
