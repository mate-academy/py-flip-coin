import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {key: 0.0 for key in range(11)}
    for _ in range(10_000):
        count = 0
        for attempt in range(10):
            count += random.choice([0, 1])
        result[count] += 1

    for key, value in result.items():
        result[key] = round((value * 100 / 10_000), 2)
    return result


def draw_gaussian_distribution_graph(dict_of_numbers: dict) -> None:
    x_coord = dict_of_numbers.keys()
    y_coord = dict_of_numbers.values()

    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")

    plt.plot(x_coord, y_coord)
    plt.show()


if __name__ == "__main__":
    simulations = flip_coin()
    print(simulations)
    draw_gaussian_distribution_graph(simulations)
