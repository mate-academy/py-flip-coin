import random


def flip_coin() -> dict:
    result_dict = {}
    for num in range(11):
        result_dict.update({num: 0})
    for case in range(10000):
        result = 0
        for time in range(10):
            res = random.randint(1, 2)
            if res == 2:
                result += 1
        result_dict[result] += 1
    for key in result_dict:
        result_dict[key] = result_dict[key] * 100 / 10000
    return result_dict

#
# def draw_gaussian_distribution_graph() -> None:
#     res_dict = flip_coin()
#     xks = list(res_dict.keys())
#     yks = list(res_dict.values())
#     xpoints = np.array(xks)
#     ypoints = np.array(yks)
#     plt.plot(xpoints, ypoints)
#     plt.ylim(0, 100)
#     plt.xlim(0, 10)
#     plt.yticks(list(range(0, 101, 10)))
#     plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
