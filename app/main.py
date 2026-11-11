import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_coin_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                      6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10_000):
        total_head_count = 0
        for _ in range(10):
            coin = random.randint(0, 1)
            total_head_count += coin
        flip_coin_dict[total_head_count] += 1
    percentage_dict = {key: round((value/10_000) * 100, 2) for
                       key, value in flip_coin_dict.items()}
    return percentage_dict


def draw_gaussian_distribution_graph(percentage_dict: dict) -> None:
    x_val = percentage_dict.keys()
    y_val = percentage_dict.values()

    plt.plot(x_val, y_val, color="blue", linestyle="-", linewidth=2)
    plt.ylim(0, 100)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
