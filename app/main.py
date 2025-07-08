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
    plt.xlabel('heads')
    plt.ylabel('Propability (%)')
    plt.title('Gaussian Distribution Graph')
    plt.xticks(range(0, 11))
    plt.show()


flip_coin()

# If you flip a coin, heads will come up 50% of the time.
# But if you flip a coin 10 times, what is the chance
# that heads will come up 5 times? 2 times?
#
# Write `flip_coin` function, that conducts at least 10000 cases
# of flipping a coin 10 times. It should return dict,
# where keys are numbers of possible heads dropped (0 to 10),
# and values are percentage of how many that number of heads
# dropped out of all cases.
# ```python
# print(flip_coin())
# # {0: 0.13, 1: 0.97, 2: 4.22, 3: 12.04, ... }
# ```
# If you have done all correctly, you should note that
# the biggest percentage of a number of heads dropped
# is about the middle, 4-6 times and tends to 0 when it is
# about the edges 0-1 and 9-10. It calls normal distribution or
# Gaussian distribution.
#
# # Extra
#
# Write `draw_gaussian_distribution_graph` function,
# that draws a graph that shows the distribution.
#
# `matplotlib` is relevant library for this purpose.
#
# - [matplotlib, Plotting](https://www.w3schools.com/python/matplotlib_plotting.asp)
# - [matplotlib, Labels](https://www.w3schools.com/python/matplotlib_labels.asp)
#
# You should get graph like this:
#
# ![gaussian](https://user-images.githubusercontent.com/80070761/152684914-6db1fcec-5c15-447f-bfce-1188eb0bb76c.png)