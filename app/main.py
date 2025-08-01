import random
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    chance_dict = {number: 0 for number in range(11)}
    for _ in range(10_000):
        orels = sum(
            1 for _ in range(10) if random.choice(("Орел", "Решка")) == "Орел"
        )
        chance_dict[orels] += 1

    for key, value in chance_dict.items():
        chance_dict[key] = round(value / 100, 2)
    return chance_dict


def draw_gaussian_distribution_graph(data: list) -> None:
    plt.plot(range(11), data)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.show()
