import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {
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


    for i in range(10000):
        current_eagles = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                current_eagles += 1
        result[current_eagles] += 1
    for key in result:
        result[key] = round((result[key] / 10000) * 100, 2)

    return result

def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_points = list(data.keys())
    y_points = list(data.values())
    plt.plot(x_points, y_points, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()
