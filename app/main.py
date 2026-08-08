import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count = 10000
    output_dict = {}

    for _ in range(count):
        output = 0
        for _ in range(10):
            coin = random.randint(0, 1)
            if coin == 1:
                output += 1
        if output not in output_dict:
            output_dict[output] = 1
        else:
            output_dict[output] += 1
    percentage_dict = {}
    for key, value in output_dict.items():
        percentage_dict[key] = round(value / count * 100, 2)
    return percentage_dict


def draw_gaussian_distribution_graph() -> None:
    flip = flip_coin()
    x_line = sorted(flip.keys())
    y_line = [flip[k] for k in x_line]
    plt.plot(x_line, y_line)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))
    plt.show()
