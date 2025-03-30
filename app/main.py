import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 0,
        10 : 0
    }

    counter = 0
    options = ["head", "eagle"]
    while counter < 10000:
        counter += 1
        heads_counter = 0
        for _ in range(10):
            if random.choice(options) == "head":
                heads_counter += 1
        result[heads_counter] += 1

    for key, value in result.items():
        result[key] = round(value * 100 / counter, 2)

    return result


"""
def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_points = data.keys()
    y_points = data.values()
    plt.plot(x_points, y_points)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.ylim(bottom=0, top=100)
    plt.show()
 """
