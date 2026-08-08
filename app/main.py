from random import choice
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(0, 10 + 1)}
    for i in range(10000):
        heads = 0
        for coin_drop in range(10):
            drop = choice([0, 1])
            if drop == 1:
                heads += 1
        result[heads] += 1
    result = {i: round(result[i] / 100, 2) for i in range(0, 10 + 1)}
    # plot(result)
    return result


# def plot(data: dict) -> None:
#     x_points = list(data.keys())
#     y_points = list(data.values())
#     plt.xlim(0, 10)
#     plt.xticks([i for i in range(0, 10 + 1)])
#     plt.yticks([i for i in range(0, 100 + 10, 10)])
#     plt.ylim(0, 100)
#     plt.plot(x_points, y_points)
#     plt.title("Gaussian Distribution")
#     plt.xlabel("Heads Count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
