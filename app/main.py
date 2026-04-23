import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    our_range = 10000
    count_heads = 0
    result_average = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                      6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for _ in range(our_range):
        for _ in range(10):
            count_heads += 1 if random.choice(coin) == "heads" else 0
        result_average[count_heads] += (1 / our_range) * 100
        count_heads = 0

    return {key: round(value, 2) for key, value in result_average.items()}

# for our graph, but matplotlib isn't in a project so tests fail on gitHub

# def draw_gaussian_distribution_graph() -> None:
#     coin_flip_results = flip_coin()
#     x_points = [key for key in coin_flip_results]
#     y_points = [value for value in coin_flip_results.values()]
#
#     plt.plot(x_points, y_points)
#     plt.yticks(range(0, 101, 10))
#     plt.xticks(range(0, 11, 1))
#     plt.xlim(0, 10)
#     plt.ylim(0, 100)
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.title("Gaussian distribution")
#
#     plt.show()
