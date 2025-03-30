import random


def flip_coin() -> dict:
    cases = 0
    come_up_list = []
    while cases < 10000:
        come_up = 0
        for _ in range(10):
            if random.choice([True, False]):
                come_up += 1
        come_up_list.append(come_up)
        cases += 1

    result = {}
    for i in set(range(11)):
        result[i] = come_up_list.count(i) / len(come_up_list) * 100
    return result


# def draw_gaussian_distribution_graph() -> None:
#     data = flip_coin()
#     x_data = np.array([key for key in data])
#     y_data = np.array([value for value in data.values()])
#
#     ax = plt.axes()
#     plt.plot(x_data, y_data)
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     ax.set_xticks(list(range(11)))
#     ax.set_yticks(list(range(0, 110, 10)))
#
#     plt.show()
