import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {k: (v / trials) * 100 for k, v in results.items()}
    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    # Extracting the keys (number of heads) and values (percentages)
    heads = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(heads, percentages, color="blue", linestyle="-", linewidth="2")

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian Distibution")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.grid(True)

    plt.show()


draw_gaussian_distribution_graph()
