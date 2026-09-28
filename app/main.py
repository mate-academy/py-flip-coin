import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0

        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads_count += 1

        result[heads_count] += 1

    for key, value in result.items():
        result[key] = round(value / 10000, 2)

    return result

def draw_gaussian_distribution_graph() -> None:
    y = [0, 1, 5, 20, 25, 20, 5, 1, 0]
    x = [0, 1, 2, 4, 5, 6, 8, 9, 10]

    plt.plot(x, y, color="blue", linewidth=2)
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
