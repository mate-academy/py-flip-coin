import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counts: dict[int, float] = {i: 0 for i in range(11)}
    for _ in range(0, 10000):
        count = 0
        for i in range(0, 10):
            heads = random.choice(["H", "T"])
            if heads == "H":
                count += 1
        counts[count] += 1

    for key, value in counts.items():
        percentage = round((value / 10000) * 100, 2)
        counts[key] = percentage
    return counts


def draw_gaussian_distribution_graph(counts: dict) -> None:
    xpoints: list[int] = list(counts.keys())
    ypoints: list[float] = list(counts.values())

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


if __name__ == "__main__":
    # Генеруємо дані
    distribution_data = flip_coin()

    # Передаємо їх у функцію малювання
    draw_gaussian_distribution_graph(distribution_data)
