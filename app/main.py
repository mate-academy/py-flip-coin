import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    number_of_cases = 10000
    flip_dict = {}
    for _ in range(number_of_cases):
        head_count = 0
        for _ in range(10):
            coin_sides = ("head", "tail")
            if random.choice(coin_sides) == "head":
                head_count += 1
        if head_count not in flip_dict:
            flip_dict[head_count] = 1 / number_of_cases * 100
        else:
            flip_dict[head_count] += 1 / number_of_cases * 100
    for key, value in flip_dict.items():
        flip_dict[key] = round(value, 2)
    return dict(sorted(flip_dict.items()))


def draw_gaussian_distribution_graph(result_flip_coin: dict) -> None:
    xpoints = list(result_flip_coin.keys())
    ypoints = list(result_flip_coin.values())
    plt.plot(xpoints, ypoints)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
