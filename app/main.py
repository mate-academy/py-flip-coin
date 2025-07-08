import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_dictionary = {}
    flip_list = [0] * 11
    for flip_round in range(10000):
        flip_set = 0
        for flip in range(0, 10):
            single_flip = random.randint(0, 1)
            if single_flip == 1:
                flip_set += 1
        flip_list[flip_set] += 1

    for i in range(11):
        flip_dictionary[i] = (flip_list[i] / 10000) * 100

    print(flip_dictionary)
    print(flip_list)
    return flip_dictionary


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    heads = list(results.keys())
    percentages = list(results.values())

    plt.bar(heads, percentages)
    plt.xlabel("heads")
    plt.ylabel("Propability (%)")
    plt.title("Gaussian Distribution Graph")
    plt.xticks(range(0, 11))
    plt.show()


flip_coin()
