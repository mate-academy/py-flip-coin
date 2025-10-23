import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    counts = {key: 0 for key in range(11)}

    for i in range(10000):
        how_many = 0
        for _ in range(10):
            coin = random.randint(0, 1)
            if coin == 1:
                how_many += 1
        counts[how_many] += 1
    result = {}
    for key, value in counts.items():
        new_value = round((value / 10000) * 100, 2)
        result[key] = new_value
    return result


def draw_gaussian_distribution_graph(positions: dict[int, float]) -> None:

    xpoint = list(positions.keys())
    ypoint = list(positions.values())

    plt.plot(xpoint, ypoint)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.title("Gaussian distribution")
    plt.show()


result_dict = flip_coin()
draw_gaussian_distribution_graph(result_dict)
