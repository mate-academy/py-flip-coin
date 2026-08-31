import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    my_dict = {x: 0 for x in range(11)}
    for _ in range(10000):
        heads_count = 0
        for i in range(10):
            coin_result = random.choice([1, 0])
            if coin_result == 1:
                heads_count += 1
        my_dict[heads_count] += 1
    for key in my_dict:
        my_dict[key] = round(((my_dict[key] / 10000) * 100), 2)

    return my_dict


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    keys = result.keys()
    values = result.values()
    plt.plot(keys, values)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
