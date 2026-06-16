import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count_flips = {}
    for i in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        if heads in count_flips:
            count_flips[heads] += 1
        else:
            count_flips[heads] = 1

    flip_dict = {}
    for flips, count in count_flips.items():
        probability = (count / 10000) * 100
        flip_dict[flips] = probability
    return flip_dict


# def draw_gaussian_distribution_graph() -> None:
#     data = flip_coin()
#     x_coord = list(data.keys())
#     y_coord = list(data.values())
#
#     plt.plot(x_coord, y_coord, linestyle="-")
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
