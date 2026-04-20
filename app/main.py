import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flipping_choice = ["HEAD", "TAIL"]
    # Create dict to store all result from FOR loop.
    iter_result = {element: 0 for element in range(11)}
    for test in range(10000):
        head = 0
        for flip in range(10):
            result = random.choice(flipping_choice)
            if result == "HEAD":
                head += 1
        iter_result[head] += 1
    return {element: iter_result[element] / 10000 * 100
            for element in iter_result
            }


# def draw_gaussian_distribution_graph(data: dict) -> None:
#     x_points = (list(data.keys()))
#     y_points = (list(data.values()))
#     plt.plot(x_points, y_points)
#     plt.show()
