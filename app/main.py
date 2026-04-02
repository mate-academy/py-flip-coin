import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    coin = ["heads", "tails"]
    result_dict: dict[int, float] = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_times = 0
        for _ in range(10):
            flip = random.choice(coin)
            if flip == "heads":
                heads_times += 1
        result_dict[heads_times] += 1

    for heads_times, values in result_dict.items():
        result_dict[heads_times] = round(values / 10000 * 100, 2)

    return result_dict


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    head_count_x = list(data.keys())
    percentage_drop_y = list(data.values())

    plt.plot(head_count_x, percentage_drop_y)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.yticks(range(0, 101, 10))
    plt.show()
