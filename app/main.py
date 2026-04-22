import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_heads = {i: 0 for i in range(11)}

    trials = 10000

    for _ in range(trials):
        heads_count = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                heads_count += 1
        flip_heads[heads_count] += 1

    for key in flip_heads:
        percentage = (flip_heads[key] / trials) * 100
        flip_heads[key] = round(percentage, 2)

    return flip_heads


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_axis = list(data.keys())
    y_axis = list(data.values())

    plt.figure(figsize=(8, 6))
    plt.plot(x_axis, y_axis, color="blue", linewidth=2)
    plt.title("Gaussian distribution", fontsize=14)
    plt.xlabel("Heads count", fontsize=12)
    plt.ylabel("Drop percentage %", fontsize=12)

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))

    plt.show()
