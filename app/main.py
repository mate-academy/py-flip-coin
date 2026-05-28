import random
import matplotlib.pyplot as plt


def flip_coin() -> dict :
    total_cases = 10000

    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    for _ in range(total_cases):
        heads_count = 0

        for _ in range(10):
            coin = random.choice(["heads", "tails"])

            if coin == "heads":
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / total_cases) * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values)

    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")

    plt.show()


data = flip_coin()

print(data)

draw_gaussian_distribution_graph(data)
