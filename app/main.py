from math import factorial
import matplotlib.pyplot as plt


def draw_gaussian_distribution_graph(num: int = 10) -> None:
    num_list = list(range(num + 1))
    graf = []
    for element in range(num + 1):
        prob = ((factorial(num) / (factorial(element)
                                   * factorial(num - element))) / (2 ** num))
        graf.append(prob * 100)  # percentage

    plt.plot(num_list, graf, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)  # force Y-axis from 0 to 100
    plt.show()


draw_gaussian_distribution_graph()
