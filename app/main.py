import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_sides = ["heads", "tails"]
    results = {}
    for i in range(10000):
        heads_drop = 0
        for toss in range(10):
            if random.choice(coin_sides) == "heads":
                heads_drop += 1

        if heads_drop in results:
            results[heads_drop] += 1
        else:
            results[heads_drop] = 1
    for key in results:
        results[key] = round(results[key] / 100, 2)
    return results


# def draw_gaussian_distribution_graph() -> None:
#     data = dict(sorted(flip_coin().items()))
#     x_points = list(data.keys())
#     y_points = list(data.values())
#
#     plt.xlim(0, 10)
#     plt.ylim(0, 100)
#
#     plt.plot(x_points, y_points)
#     plt.show()
