import random
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000) -> dict:
    heads_count = {i: 0 for i in range(11)}

    for case in range(cases):

        heads_in_case = 0
        for flip in range(10):
            if random.random() < 0.5:
                heads_in_case += 1

        heads_count[heads_in_case] += 1

    result = {}
    for heads, count in heads_count.items():
        percentage = (count / cases) * 100
        result[heads] = round(percentage, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin(10000)

    not_single_letter_x = list(data.keys())
    not_single_letter_y = list(data.values())

    plt.plot(not_single_letter_x, not_single_letter_y)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
