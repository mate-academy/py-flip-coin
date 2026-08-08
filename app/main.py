import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1
        results[heads_count] += 1

    return {heads: (count / cases) * 100 for heads, count in results.items()}


def distribution_graph(distribution_dict: dict) -> None:
    x_values = list(distribution_dict.keys())
    y_values = list(distribution_dict.values())

    plt.plot(x_values, y_values)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.grid(True, alpha=0.3)

    plt.show()


if __name__ == "__main__":
    data = flip_coin()

    print(data)

    distribution_graph(data)
