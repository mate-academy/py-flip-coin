import random
import matplotlib.pyplot as plt


def flip_coin(cases : int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads += 1

        results[heads] += 1

    percentage = {
        heads: round(results[heads] / cases * 100, 2)
        for heads, count in results.items()
    }

    return percentage


def draw_gaussian_distribution_graph(data: dict) -> None:
    xs = list(data.keys())
    ys = list(data.values())

    plt.figure(figsize=(8, 5))
    plt.bar(xs, ys)

    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads in 10 coin flips")

    plt.xticks(range(11))
    plt.show()


result = flip_coin()
print(result)
draw_gaussian_distribution_graph(result)
