import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}
    count_iteration = 100000
    for i in range(count_iteration):
        sum_heads = 0
        for _ in range(10):
            heads_or_tails = random.randint(0, 1)
            if heads_or_tails == 1:
                sum_heads += 1
        result[sum_heads] += 1
    result = {key: round((value / count_iteration) * 100, 2)
              for key, value in result.items()}

    return result


def draw_gaussian_distribution_graph() -> None:
    date_heads = flip_coin()
    coord_x = list(date_heads.keys())
    coord_y = list(date_heads.values())
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(coord_x, coord_y, color="blue")


draw_gaussian_distribution_graph()