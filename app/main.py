from random import randint
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def flip_coin():
    number_of_trials = 10
    number_of_coin_tosses = 10000

    trials = [
        sum([randint(0, 1) for _ in range(number_of_trials)])
        for _ in range(number_of_coin_tosses)
    ]
    freq = [trials.count(k) / 100 for k in range(number_of_trials + 1)]

    x_major_locator = MultipleLocator(1)
    y_major_locator = MultipleLocator(10)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.axis([0, 10, 0, 100])
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')

    plt.plot(range(number_of_trials + 1), freq, color="blue")
    plt.show()


flip_coin()
