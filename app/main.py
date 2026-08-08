import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads = []
    i = 1
    heads_dict = {}

    while i <= 10000:
        head = 0
        for _ in range(10):
            toss_a_coin = random.choice(["H", "T"])
            if toss_a_coin == "H":
                head += 1
        i += 1
        heads.append(head)

    keys = set(heads)
    for key in sorted(keys):
        heads_dict[key] = round(heads.count(key) / 10000 * 100, 2)

    return heads_dict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_cor = list(data.keys())
    y_cor = list(data.values())

    plt.bar(x_cor, y_cor)
    plt.xlabel("Head count")
    plt.ylabel("Drop percentage %")
    plt.show()
