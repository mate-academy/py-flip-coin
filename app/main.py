import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_dict = {i: 0 for i in range(11)}
    for _ in range(10000):
        counter = 0
        for i in range(0, 10):
            if random.randint(0, 1) == 1:
                counter += 1
        coin_dict[counter] += 1
    result = {}
    for key, value in coin_dict.items():
        percent = round((value / 10000) * 100, 2)
        result[key] = percent
    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_point = list(data.keys())
    y_point = list(data.values())
    plt.figure(figsize=(10, 10))
    plt.plot(x_point, y_point)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


result = flip_coin()
draw_gaussian_distribution_graph(result)
