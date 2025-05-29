import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_dict = {key: 0 for key in range(11)}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            head = random.randint(0, 1)
            if head == 1:
                count += 1
        heads_dict[count] += 1

    for key in heads_dict:
        heads_dict[key] = round((heads_dict[key] * 100) / 10000, 2)
    return heads_dict


def draw_gaussian_distribution_graph() -> None:
    head = flip_coin()
    x_point = list(head.keys())
    y_point = list(head.values())
    plt.title("Gaussian distribution")
    plt.plot(x_point, y_point, color="blue")
    plt.ylim(0, 100)
    plt.xlabel("Head count")
    plt.ylabel("Drop percentage %")
    plt.show()
