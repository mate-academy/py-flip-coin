import matplotlib.pyplot as plt
import random

def flip_coin() -> dict:
    eagle_dict = {i: 0 for i in range(11)}
    for experiment in range(10000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        eagle_dict[heads] += 1
    for k in eagle_dict:
        eagle_dict[k] = eagle_dict[k] / 10000 * 100
    return eagle_dict

result = flip_coin()

def draw_gaussian_distribution_graph(eagle_dict) -> None:
    x = eagle_dict.keys()
    y = eagle_dict.values()
    plt.plot(x, y, marker = 'o')
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.show()

draw_gaussian_distribution_graph(result)
