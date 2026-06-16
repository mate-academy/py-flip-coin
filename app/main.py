# import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    trials = 10000
    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    return {key: (value / trials) * 100 for key, value in results.items()}


# def draw_gaussian_distribution_graph(flip_heads: dict) -> None:
#     plt.plot(list(flip_heads.keys()), list(flip_heads.values()), color="red")
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.ylim(0, 100)
#     plt.xlim(0, 10)
#     plt.show()
#
#
# draw_gaussian_distribution_graph(flip_coin())
