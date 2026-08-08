import random


def flip_coin() -> dict[int, float]:
    count_heads_dropped: dict[int, float] = {i: 0 for i in range(11)}
    for _ in range(10_000):
        heads_random = [random.randint(0, 1) for _ in range(10)].count(1)
        count_heads_dropped[heads_random] += 1

    for key in count_heads_dropped:
        count_heads = count_heads_dropped[key]
        count_heads_dropped[key] = round((count_heads / 10_000) * 100, 2)

    return count_heads_dropped


# def draw_gaussian_distribution_graph(func: dict[int, float]) -> None:
#     axis_x = np.array(list(func.keys()))
#     axis_y = np.array(list(func.values()))
#
#     plt.plot(axis_x, axis_y)
#
#     plt.ylim(0, 100)
#     plt.xlim(min(axis_x), max(axis_x))
#
#     font1 = {"family": "serif", "color": "blue", "size": 20}
#
#     plt.title("Gaussian distribution", fontdict=font1)
#     plt.ylabel("Drop percentage %")
#     plt.xlabel("Heads count")
#
#     plt.show()
