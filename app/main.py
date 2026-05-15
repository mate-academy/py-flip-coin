import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_dict = {key: 0 for key in range(11)}
    for _ in range(10_000):
        counter_heads = 0
        for flip in range(10):
            head = random.randint(0, 1)
            if head == 1:
                counter_heads += 1
        heads_dict[counter_heads] += 1

    for value in heads_dict:
        heads_dict[value] = round((heads_dict[value] / 10000) * 100, 2)
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
