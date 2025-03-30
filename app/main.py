import random
import matplotlib.pylab as plt


def flip_coin():
    result = {key: 0 for key in range(11)}
    for i in range(10000):
        head = 0
        for j in range(10):
            side_of_coin = random.choice(["head", "tail"])
            if side_of_coin == "head":
                head += 1
        result[head] += 1
    final_result = {key: (value / 10000) * 100
                    for key, value in result.items()}
    return final_result


def draw_gaussian_distribution_graph():
    coordinates = flip_coin()
    x = [key for key in coordinates.keys()]
    y = [value for value in coordinates.values()]
    plt.plot(x, y, color='blue', linestyle='solid')
    plt.xlim([0, 10])
    plt.ylim([0, 100])
    plt.yticks(range(0, 110, 10))
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.title('Gaussian distribution')
    plt.show()
