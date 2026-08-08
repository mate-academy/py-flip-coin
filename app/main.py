import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    probabilities = {
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
    for _ in range(10000):
        heads = 0
        for _ in range(0, 10):
            if random.randint(0, 1):
                heads += 1
        probabilities[heads] += 1

    for key, value in probabilities.items():
        probabilities[key] = round(value / 10000 * 100, 2)

    return probabilities


# def draw_gaussian_distribution_graph(data: dict) -> None:
#     plt.xlim(0, 10)
#     plt.ylim(0, 100)
#     plt.xticks(range(0, 11))
#     plt.yticks(range(0, 101, 10))
#     plt.plot(data.keys(), data.values())
#
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.title("Gaussian distribution")
#
#     plt.show()
