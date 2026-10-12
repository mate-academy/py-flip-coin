import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    total_experiments = 10000
    counts = {i: 0 for i in range(11)}

    for _ in range(total_experiments):
        heads = sum(random.randint(0, 1) for _ in range(10))
        counts[heads] += 1

    percentages = {
        heads: (count / total_experiments) * 100
        for heads, count in counts.items()
    }
    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads_counts = list(data.keys())
    drop_percentages = list(data.values())

    plt.figure(figsize=(8, 6))
    plt.plot(heads_counts, drop_percentages, color="blue")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))

    plt.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)
    plt.show()


print(flip_coin())
