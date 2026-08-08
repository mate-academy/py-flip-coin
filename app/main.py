import random

# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_coin_dict = {}
    times = 10000

    for _ in range(times):
        count_head = 0
        for _ in range(10):
            count_head += random.randint(0, 1)
        if count_head not in flip_coin_dict.keys():
            flip_coin_dict[count_head] = 1
        else:
            flip_coin_dict[count_head] += 1

    for key, value in flip_coin_dict.items():
        flip_coin_dict[key] = round(value / times * 100, 2)

    return dict(sorted(flip_coin_dict.items()))


# def draw_gaussian_distribution_graph() -> None:
#     gauss = flip_coin()
#
#     coord_x = list(gauss.keys())
#     coord_y = list(gauss.values())
#
#     plt.plot(coord_x, coord_y)
#
#     plt.title("Gaussian distributions")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#
#     plt.show()
