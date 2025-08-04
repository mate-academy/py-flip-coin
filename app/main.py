import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    side = ["head", "teil"]
    stat = {i: 0 for i in range(0, 11)}
    for _ in range(10000):
        count = 0
        for attempt in range(10):
            res = random.choice(side)
            if res == "head":
                count += 1
        stat[count] += 1
    for key, value in stat.items():
        stat[key] = round(value / 100, 2)
    return stat


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_axis = list(data.keys())
    y_axis = list(data.values())

    plt.plot(x_axis, y_axis)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(0, 11, 1))
    plt.step_y = 10
    plt.step_x = 1
    plt.show()


data = flip_coin()
draw_gaussian_distribution_graph(data)
