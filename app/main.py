import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    number_of_heads = [
        [
            random.randint(0, 1) for _ in range(10)
        ].count(0) for _ in range(10000)
    ]
    result = {
        0: (number_of_heads.count(0) / 10000) * 100,
        1: (number_of_heads.count(1) / 10000) * 100,
        2: (number_of_heads.count(2) / 10000) * 100,
        3: (number_of_heads.count(3) / 10000) * 100,
        4: (number_of_heads.count(4) / 10000) * 100,
        5: (number_of_heads.count(5) / 10000) * 100,
        6: (number_of_heads.count(6) / 10000) * 100,
        7: (number_of_heads.count(7) / 10000) * 100,
        8: (number_of_heads.count(8) / 10000) * 100,
        9: (number_of_heads.count(9) / 10000) * 100,
        10: (number_of_heads.count(10) / 10000) * 100
    }

    return result


def draw_gaussian_distribution_graph() -> None:
    plt.plot(list(flip_coin().keys()), list(flip_coin().values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
aaaa