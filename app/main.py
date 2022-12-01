import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_coin_list = ["heads", "tails"]
    experiment_data = {i: 0 for i in range(11)}

    for _ in range(10000):
        count_of_flip = 0
        for flip in range(10):
            if random.choice(flip_coin_list) == "heads":
                count_of_flip += 1
            count_of_flip += 0
        experiment_data[count_of_flip] += 1

    for key, value in experiment_data.items():
        experiment_data[key] = value / 100

    return experiment_data


def draw_gaussian_distribution_graph() -> None:
    plt.plot(list(flip_coin().keys()), list(flip_coin().values()))
    plt.title("Flipping coin")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
