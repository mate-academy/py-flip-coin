import random
# import matplotlib as mpl
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    number_of_cases = 10000
    number_of_attempt = 10
    result_dict = {flip: 0 for flip in range(number_of_attempt + 1)}
    for _ in range(number_of_cases):
        experiment_flips = 0
        for attempt in range(number_of_attempt):
            if random.choice([0, 1]) == 0:
                experiment_flips += 1
        result_dict[experiment_flips] += 1
    for iter_, value in result_dict.items():
        result_dict[iter_] = value / 100
    return result_dict


# def draw_gaussian_distribution_graph() -> None:
#     dpi = 80
#     fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
#     mpl.rcParams.update({"font.size": 10})
#
#     plt.axis([0, 10, 0, 100])
#
#     plt.title("Gaussian Distribution")
#     plt.xlabel("Number of flips")
#     plt.ylabel("Drop percentage %")
#
#     plt.plot(flip_coin().values(), color="blue", linestyle="solid",
#              label="flips")
#
#     plt.legend(loc="upper right")
#     fig.savefig("flip.png")
