import matplotlib.pyplot as plt


def draw_gaussian_distribution_graph(outcomes_percentage: dict) -> None:
    keys = list(outcomes_percentage.keys())
    values = [max(0.01, v) for v in outcomes_percentage.values()]
    plt.figure(figsize=(10, 6))
    plt.bar(keys, values, color="skyblue", edgecolor="black")
    plt.title("Gaussian_distribution", fontsize=16)
    plt.xlabel("Heads count", fontsize=14)
    plt.ylabel("Drop percentage %", fontsize=14)
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
