import random
from matplotlib import pyplot as plt


def flip_coin(number):
    counters = {i: 0 for i in range(11)}
    for _ in range(number):
        count = 0
        for __ in range(10):
            if random.random() < 0.5:
                count += 1
        counters[count] += 1
    for k in counters:
        percentage =  counters[k] / number * 100
        counters[k] = round(percentage, 2)
    return counters

def draw_gaussian_distribution_graph(number):
    data = flip_coin(number)

    x = list(data.keys())
    y = list(data.values())

    plt.figure()
    plt.plot(x, y, marker='o')
    plt.xlabel("Number of heads in 10 flips")
    plt.ylabel("Percentage")
    plt.title(f"Coin flip distribution ({number} experiments)")
    plt.grid(True)
    plt.show()

print(flip_coin(10000))
draw_gaussian_distribution_graph(10000)

