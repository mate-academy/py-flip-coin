import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_tails = ("Heads", "Tails")
    dct_heads_occurrence = {i: 0 for i in range(11)}
    for _ in range(10000):
        ten_head_tails = random.choices(heads_tails, k=10)
        dct_heads_occurrence[ten_head_tails.count("Heads")] += 1
    return {
        key: round(value / 10000 * 100, 2)
        for key, value in dct_heads_occurrence.items()
    }


def draw_gaussian_distribution_graph() -> None:
    plt.plot(list(flip_coin().keys()), list(flip_coin().values()))
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop percentage %")
    plt.show()
